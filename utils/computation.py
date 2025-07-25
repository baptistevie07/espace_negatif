import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import Voronoi
from scipy.spatial import cKDTree
from collections import defaultdict
import time
from itertools import combinations

class Computation():
    def __init__(self):
        self.points = None
        self.tri = None
        self.triangle_counts = None
        self.areas = None
        self.candidates = None
        self.empty_triangles = None
        self.candidates_triangles = None
        self.region_empty = None
        self.region_candidates = None
        self.tree = None  # cKDTree pour les recherches de voisinage
        self.neighbors = None  # Dictionnaire pour les voisins de Delaunay

    def afficher(self, id_to_track, candidates, message):
        #si candidates est un dictionnaire, on prend les clés et on en fait des int
        if isinstance(candidates, dict):
            candidates = list(candidates.keys())
        # Now id_to_track is a list
        if not all(x in candidates for x in id_to_track):  # inclusion
            lost_ids = [id for id in id_to_track if id not in candidates]
            print("Perte de candidats : ", message, " : ", lost_ids)
            return [id for id in id_to_track if id in candidates]
        if not candidates:
            print(f"Aucun candidat trouvé pour {message}.")
            return id_to_track
        return []
    def build_delaunay_neighbors(self,tri):
        neighbors = defaultdict(set)
        for triangle in tri.simplices:
            for i in range(3):
                a, b = triangle[i], triangle[(i + 1) % 3]
                neighbors[a].add(b)
                neighbors[b].add(a)
        return neighbors
    def has_distant_delaunay_neighbors(self,idx, points, delaunay_neighbors, min_dist=2.0, min_count=2):
        count = 0
        p = points[idx]
        for neighbor_idx in delaunay_neighbors[idx]:
            dist = np.linalg.norm(p - points[neighbor_idx])
            if dist >= min_dist:
                count += 1
                if count >= min_count:
                    return True
        return False
    def compte_voisins_communs(self,triangle_counts, distance_threshold=0.4):
        # Étape 1 — associer à chaque point la liste des triangles auxquels il appartient
        point_to_triangles = defaultdict(set)

        for i, tri_pts in enumerate(self.tri.simplices):
            for pt in tri_pts:
                point_to_triangles[pt].add(i)

        # Étape 2 — préparer adjusted_counts (copie initiale)
        adjusted_counts = {idx: len(point_to_triangles[idx]) for idx in triangle_counts}

        # Étape 3 — fusionner les voisins proches
        indices = list(adjusted_counts.keys())

        for a, b in combinations(indices, 2):
            #print(f"Comparaison des points {a} et {b} avec distance {np.linalg.norm(self.points[a] - self.points[b]):.2f}")
            if np.linalg.norm(self.points[a] - self.points[b]) < distance_threshold:
                # union des triangles
                union_tris = point_to_triangles[a] | point_to_triangles[b]
                new_count = len(union_tris)
                #print(f"Points {a} et {b} fusionnés, nouveau compte : {new_count} (ancien : {adjusted_counts[a]}, {adjusted_counts[b]})")
                adjusted_counts[a] = max(adjusted_counts[a], new_count)
                adjusted_counts[b] = max(adjusted_counts[b], new_count)
        return adjusted_counts

    def computation(self, positions, ages, width, height):
        points = np.array([pos for pos in positions.values() if pos is not None])
        ages = np.array([ages[obj] for obj in positions.keys() if positions[obj] is not None])
        if len(points) < 3:
            print(f"\rPas assez de points uniques pour la triangulation (avant filtrage).", end="")
            return None
        mask = ((points[:, 0] >= 0) & (points[:, 0] <= width) &
                (points[:, 1] >= 0) & (points[:, 1] <= height) & (ages > 5))
        points = points[mask]
        points = np.unique(points, axis=0)
        if len(points) < 3:
            print(f"\rPas assez de points uniques pour la triangulation (après filtrage).", end="")
            return None
        points_a_exclure = []###############################################
        points = np.array([point for i, point in enumerate(points) if i not in points_a_exclure])
        tri = Delaunay(points)
        triangle_counts = defaultdict(int)
        for simplex in tri.simplices:
            for vertex in simplex:
                triangle_counts[vertex] += 1
        vor = Voronoi(points)
        areas = {}
        for idx, region_index in enumerate(vor.point_region):
            region = vor.regions[region_index]
            if not -1 in region and len(region) > 0:
                polygon = [vor.vertices[i] for i in region]
                area = 0.5 * np.abs(
                    np.dot([p[0] for p in polygon], np.roll([p[1] for p in polygon], 1)) -
                    np.dot([p[1] for p in polygon], np.roll([p[0] for p in polygon], 1))
                )
                areas[idx] = area
            else:
                areas[idx] = np.inf
        # Mise à jour des variables de la classe
       
        self.points = points
             
        
        self.tri = tri
        self.tree = cKDTree(points)
        self.neighbors = self.build_delaunay_neighbors(tri)
        #print(f"Triangulation Delaunay effectuée avec {len(tri.simplices)} triangles.")
             
        
        self.triangle_counts = triangle_counts
             
        
        self.areas = areas
             
        
        return None
    def filtrage_angulaire(self,filtered_candidates,angle_max,id_to_track):
        # Étape 1 – identifier les candidats avec angles > 120°, à exclure du cœur mais à garder comme "contour"
        contour_candidates = set()
        core_candidates = []
        for idx in filtered_candidates:
            point = self.points[idx]
            angles = []
            other_indices = []

            for other_idx, other_point in enumerate(self.points):
                if other_idx == idx:
                    continue
                vector = other_point - point
                angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi + 180
                angles.append(angle)
                other_indices.append(other_idx)

            if len(angles) < 2:
                continue

            angles = np.array(angles)
            sorted_indices = np.argsort(angles)
            sorted_angles = angles[sorted_indices]
            sorted_neighbors = [other_indices[i] for i in sorted_indices]

            diffs = np.diff(sorted_angles)
            last_diff = 360 + sorted_angles[0] - sorted_angles[-1]
            diffs = np.append(diffs, last_diff)

            if np.max(diffs) > 120:
                contour_candidates.add(idx)
                if idx in id_to_track:
                    print(f"Point {idx} dégradé en contour pour grand angle initial : {np.max(diffs):.1f}°")
            else:
                core_candidates.append(idx)
        # Étape 2 – filtrage des core_candidates avec les points du contour comme "référence angulaire"
        final_candidates = []

        extended_non_candidates = (set(range(len(self.points))) - set(core_candidates)) | contour_candidates

        for idx in core_candidates:
            point = self.points[idx]
            angles = []
            other_indices = []

            for other_idx in extended_non_candidates:
                if other_idx == idx:
                    continue
                vector = self.points[other_idx] - point
                angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi + 180
                angles.append(angle)
                other_indices.append(other_idx)

            if len(angles) < 2:
                continue

            angles = np.array(angles)
            sorted_indices = np.argsort(angles)
            sorted_angles = angles[sorted_indices]
            sorted_neighbors = [other_indices[i] for i in sorted_indices]

            diffs = np.diff(sorted_angles)
            last_diff = 360 + sorted_angles[0] - sorted_angles[-1]
            diffs = np.append(diffs, last_diff)

            keep = True
            
            for i, delta in enumerate(diffs):
                if delta < angle_max:
                    continue
                #print(f"Point {idx} rejeté pour angle suspect {delta:.1f}°")
                a_idx = sorted_neighbors[i]
                b_idx = sorted_neighbors[(i + 1) % len(sorted_neighbors)]

                d_ab = np.linalg.norm(self.points[a_idx] - self.points[b_idx])
                d_ai = np.linalg.norm(self.points[a_idx] - point)
                d_bi = np.linalg.norm(self.points[b_idx] - point)
                if not (d_ai < 0.9 * d_ab and d_bi < 0.9 * d_ab):
                    keep = False
                    if idx in id_to_track:
                        print(f"Point {idx} rejeté pour angle suspect {delta:.1f}° entre {a_idx} et {b_idx}")
                    break
                if d_ab> 2.5:
                    keep = False
                    if idx in id_to_track:
                        print(f"Point {idx} rejeté pour angle suspect {delta:.1f}° entre {a_idx} et {b_idx} (distance {d_ab:.2f} > 2.5)")
                    break

            if keep:
                final_candidates.append(idx)
        # On a trouvé des candidats, si deux sont très proches, si un est gardé, on garde l'autre
        if not final_candidates:
            return []
        if  len(final_candidates) == len(filtered_candidates):
            return final_candidates
        point_to_triangles = defaultdict(set)

        for i, tri_pts in enumerate(self.tri.simplices):
            for pt in tri_pts:
                point_to_triangles[pt].add(i)

        for a, b in combinations(filtered_candidates, 2):
            #print(f"Comparaison des points {a} et {b} avec distance {np.linalg.norm(self.points[a] - self.points[b]):.2f}")
            if np.linalg.norm(self.points[a] - self.points[b]) < 0.5:
                print(f"Points {a} et {b} très proches, vérification des triangles")
                if a in final_candidates and b not in final_candidates:
                    final_candidates.append(b)
                    if b in id_to_track:
                        print(f"Point {b} conservé car proche de {a}")
                elif b in final_candidates and a not in final_candidates:
                    final_candidates.append(a)
                    if a in id_to_track:
                        print(f"Point {a} conservé car proche de {b}")
        return final_candidates

    def personnes_centrales(self, n_triangles, distance_min, angle_max, id_to_track=[]):
        
        points = self.points
        tri = self.tri
        triangle_counts = self.triangle_counts
        areas = self.areas

        if tri is None or triangle_counts is None:
            self.candidates = None
            self.candidates_triangles = None
            return None
        #print(f"debut personnes_centrales avec {len(self.tri.simplices)} triangles")
        #si deux candidats sont très proches, alors on leur donne à tous les deux le nombre de voisins commun
        shared_counts = self.compte_voisins_communs(triangle_counts,distance_threshold=0.4)
        candidates = {idx: count for idx, count in shared_counts.items() if areas.get(idx, np.inf) != np.inf}
        
        id_to_track = self.afficher(id_to_track, candidates, "aire infinie")
        if not candidates:
            self.candidates = None
            self.candidates_triangles = None
            return None
        weak_candidates = {idx: count for idx, count in shared_counts.items() if n_triangles-2<=count<n_triangles}
        #print("weak",weak_candidates)
        candidates = {idx: count for idx, count in candidates.items() if count >= n_triangles}
        #print("central",candidates)
        #Si un candidat faible est relié à un autre faible ou à un fort, on le garde
        for idx, count in weak_candidates.items():
            for neighbor_idx in self.neighbors[idx]:
                if neighbor_idx in candidates or neighbor_idx in weak_candidates:
                    candidates[idx] = count
                    if idx in id_to_track:
                        print(f"Point {idx} conservé car relié à un autre candidat")
                    break
        id_to_track = self.afficher(id_to_track, candidates, f"moins de {n_triangles} triangles")
        
        if not candidates:
            self.candidates = None
            self.candidates_triangles = None
            return None
        candidate_indices = list(candidates.keys())
        filtered_candidates = []
        for idx in candidate_indices:
            point = points[idx]
            is_far = True
            for other_idx, other_point in enumerate(points):
                if other_idx not in candidate_indices:
                    distance = np.linalg.norm(point - other_point)
                    if distance < distance_min:
                        is_far = False
                        break
            if is_far:
                filtered_candidates.append(idx)
        filtered_candidates = list(set(filtered_candidates))
        id_to_track = self.afficher(id_to_track, filtered_candidates, f"proche d'un autre point (distance < {distance_min})")
        if len(filtered_candidates) == 0:
            self.candidates = None
            self.candidates_triangles = None
            return None
        #if len(filtered_candidates) == 1:
         #   if self.candidates != filtered_candidates:
          #      self.candidates = filtered_candidates
           #     return filtered_candidates
            #return None
        
        # Étape 3 – filtrage angulaire
        final_candidates = self.filtrage_angulaire(filtered_candidates, angle_max, id_to_track)

        id_to_track = self.afficher(id_to_track, final_candidates, f"angle max {angle_max}°")
        delaunay_neighbors = self.neighbors
        final2_candidates = []
        for idx in final_candidates:
            if self.has_distant_delaunay_neighbors(idx, points, delaunay_neighbors, min_dist=3, min_count=2):
                final2_candidates.append(idx)
        #On regarde les candidats non retenus, et on les garde si ils ont des voisins candidats qui ont été retenus
        for idx in final_candidates:
            if idx in final2_candidates:
                continue
            # Vérifier si ce point a des voisins candidats qui ont été retenus
            has_candidate_neighbor = False
            for neighbor_idx in delaunay_neighbors[idx]:
                if neighbor_idx in final2_candidates and np.linalg.norm(points[idx] - points[neighbor_idx]) < 1.5:
                    has_candidate_neighbor = True
                    break
            if has_candidate_neighbor:
                final2_candidates.append(idx)
                if idx in id_to_track:
                    print(f"Point {idx} conservé car voisin candidat retenu")
        id_to_track = self.afficher(id_to_track, final2_candidates, f"voisins éloignés (distance >= 2.0)")

        # prend final2_candidates comme candidats finaux, on en fait une liste de liste et dans ses sous-listes, on rassemble les candidats très proches, que l'on traitera ensemble
        if not final2_candidates:
            self.candidates = None
            self.candidates_triangles = None
            return None
        final2_candidates = list(set(final2_candidates))
        grouped_candidates = []
        already_grouped = set()
        for candidate in final2_candidates:
            if candidate in already_grouped:
                continue
            group = [candidate]
            for other_candidate in final2_candidates:
                if other_candidate != candidate and other_candidate not in already_grouped:
                    if np.linalg.norm(points[candidate] - points[other_candidate]) < 0.5:
                        group.append(other_candidate)
                        already_grouped.add(other_candidate)
            grouped_candidates.append(group)
        

        self.candidates_triangles = []
        for group in grouped_candidates:
            candidates_triangles = {}
            idx=0
            for simplex in self.tri.simplices:
                if any(vertex in group for vertex in simplex):
                    candidates_triangles[idx] = simplex.tolist()
                idx+=1
            self.candidates_triangles.append(candidates_triangles)
        
        #print(f"nombre de triangles candidats : {len(self.candidates_triangles[0])}")
        self.candidates = final2_candidates
        
        
        
        return None

    def empty_zones(self, area_threshold=2, radius=2):
        
        points = self.points
        tri = self.tri
        if tri is None or points is None:
            return None
        #print(f"debut empty_zones avec {len(self.tri.simplices)} triangles")
        empty_triangles = {}
        idx = 0
        for simplex in tri.simplices:
            
            pts = points[simplex]
            area = 0.5 * np.abs(
                np.dot([p[0] for p in pts], np.roll([p[1] for p in pts], 1)) -
                np.dot([p[1] for p in pts], np.roll([p[0] for p in pts], 1))
            )
            if area > area_threshold:
                empty_triangles[idx] = simplex.tolist()
            idx += 1
        
        
        # Parmis ces candidats, on va vérifier que tous les sommets ont au moins 2 voisins proches
        #print(f"Nombre de triangles vides trouvés : {len(empty_triangles)}")
        if not empty_triangles or self.tree== None:
            self.empty_triangles = None
            return None
        filtered_empty_triangles = {}
        print(f"triangles vides trouvés : {empty_triangles}")

        
        for id,triangle in empty_triangles.items():
            potentiel = True
            for i in triangle:
                # Chercher tous les points dans le rayon autour du sommet
                neighbor_ids = self.tree.query_ball_point(points[i], r=radius)
                
                valid_neighbors = [nid for nid in neighbor_ids if nid != i]
                print(f"Point {i} a {len(valid_neighbors)} voisins proches dans le triangle {id}, radius {radius}")
                if len(valid_neighbors) < 2: #Au moins deux voisins proches
                    potentiel = False
            if potentiel:
                filtered_empty_triangles[id] = triangle
        #On fait comme pour les candidats, on regroupe les triangles vides par groupe de triangles proches, à la fin on obtient une liste de dictionnaires de triangles adjacents
        visited_triangles = set()
        grouped_empty_triangles = []
        for triangle_id, triangle in filtered_empty_triangles.items():
            if triangle_id in visited_triangles:
                continue
            group = {triangle_id: triangle}
            visited_triangles.add(triangle_id)
            for other_triangle_id, other_triangle in filtered_empty_triangles.items():
                if other_triangle_id == triangle_id or other_triangle_id in visited_triangles:
                    continue
                # Vérifier si les triangles partagent un sommet
                if set(triangle) & set(other_triangle):
                    group[other_triangle_id] = other_triangle
                    visited_triangles.add(other_triangle_id)
            grouped_empty_triangles.append(group)
        self.empty_triangles = grouped_empty_triangles
        #print(f"Nombre de triangles vides filtrés : {len(self.empty_triangles)}")
        if len(self.empty_triangles) == 0:
            self.empty_triangles = None
            return None
        print(f"Nombre de triangles vides filtrés : {len(self.empty_triangles)}")
        return None

    def edge_length(self, p1, p2):
        return np.linalg.norm(p1 - p2)

    def get_edge_indices(self, triangle):
        return [(triangle[0], triangle[1]),
                (triangle[1], triangle[2]),
                (triangle[2], triangle[0])]
    def compute_region_perimeter(self,region):
        edge_counts = defaultdict(int)
        total_area = 0
        # Étape 1 : compter toutes les arêtes
        for tri_idx in region:
            triangle = self.tri.simplices[tri_idx]
            edges = [
                tuple(sorted((triangle[0], triangle[1]))),
                tuple(sorted((triangle[1], triangle[2]))),
                tuple(sorted((triangle[2], triangle[0]))),
            ]
            for edge in edges:
                edge_counts[edge] += 1
            #calcul de l'aire du triangle
            pts = self.points[triangle]
            total_area += 0.5 * np.abs(
                np.dot([p[0] for p in pts], np.roll([p[1] for p in pts], 1)) -
                np.dot([p[1] for p in pts], np.roll([p[0] for p in pts], 1))
            )

        # Étape 2 : garder uniquement les arêtes uniques (bord)
        border_edges = [edge for edge, count in edge_counts.items() if count == 1]

        # Étape 3 : calculer la somme des longueurs
        perimeter = 0
        max_edge = 0
        for a, b in border_edges:
            perimeter += np.linalg.norm(self.points[a] - self.points[b])
            if np.linalg.norm(self.points[a] - self.points[b]) > max_edge:
                max_edge = np.linalg.norm(self.points[a] - self.points[b])

        return max_edge,perimeter, border_edges,total_area

    def expansion(self,triangles, type,ratio_threshold,min_density,nb_min_region=4,ratio_area=1.4):
        points = self.points
        tri = self.tri
        #print(f"triangles keys : {triangles.keys()}")
        region = set(triangles.keys())
        visited = set()
        to_visit = list(region)
        #print(f"to visit :{to_visit}")
        while to_visit:
            #nb_iterations-=1
            #if nb_iterations <= 0:
                #break
            current_idx = to_visit.pop()
            visited.add(current_idx)
            current_triangle = tri.simplices[current_idx]

            for neighbor_pos, neighbor_idx in enumerate(tri.neighbors[current_idx]):
                if neighbor_idx == -1 or neighbor_idx in visited or neighbor_idx in region:
                    continue

                neighbor_triangle = tri.simplices[neighbor_idx]

                # Trouver l’arête commune via les indices partagés
                shared_vertices = set(current_triangle) & set(neighbor_triangle)
                if len(shared_vertices) != 2:
                    continue  # doit partager une arête complète

                a, b = list(shared_vertices)
                edge = self.edge_length(points[a], points[b])

                # Sommet restant dans le triangle voisin
                other = list(set(neighbor_triangle) - shared_vertices)[0]

                d1 = self.edge_length(points[a], points[other])
                d2 = self.edge_length(points[b], points[other])

                if d1 + d2 < ratio_threshold * edge:
                    region.add(neighbor_idx)
                    to_visit.append(neighbor_idx)
                    #print(f"Ajout du triangle {neighbor_idx} à la région {type}")
        # Update the region attribute of the class
        #print(f"Région trouvée de type {type} avec {region} triangles sur un total de {len(self.tri.simplices)} triangles.")
        #calcul de la ratio nb de personnes du contour / perimetre
        max_edge, perimeter, border_edges,total_area = self.compute_region_perimeter(region)
        density = perimeter/len(border_edges) if perimeter > 0 else 0
        #print(f"Densité de la région {type} : {density:.2f} (nombre de bords : {len(border_edges)}, périmètre : {perimeter:.2f})")
        if type == "expansion_candidate":
            #print(f"candidates : {self.candidates},border_edges : {len(border_edges)}, perimeter : {perimeter:.2f}, total_area : {total_area:.2f}, ratio_area : {ratio_area}")
            #print(f"inegalité : {perimeter*perimeter:.2f} > 1.4*4*3.14*{total_area:.2f} = {1.4*4*3.14*total_area:.2f}")
            if (len(region) < nb_min_region or density > min_density or max_edge > 3 
            #or len(self.candidates)*4 >= len(border_edges) 
            or perimeter*perimeter>ratio_area*4*3.14*total_area
            or len(border_edges)<7): #Il faut au moins 4 fois plus de bords que de candidats pour l'expansion
                if True:
                    if  perimeter*perimeter>ratio_area*4*3.14*total_area:
                        print(f"inegalité : {perimeter*perimeter:.2f} > {ratio_area}*4*3.14*{total_area:.2f} = {ratio_area*4*3.14*total_area:.2f}")
                    if len(border_edges)<7:
                        print(f"Pas assez de bords pour l'expansion candidates (seulement {len(border_edges)} trouvés).")
                    if density > min_density:
                        print(f"Densité trop élevée pour l'expansion candidates : {density:.2f}, min : {min_density} (périmètre : {perimeter:.2f}, nombre de bords : {len(border_edges)})")
                    if max_edge > 3:
                        print(f"Expansion candidates rejetée car le côté maximal {max_edge:.2f} est supérieur à 3.")
                    if len(region) < nb_min_region:
                        print(f"Pas assez de triangles candidats pour l'expansion candidates (seulement {len(region)} trouvés).")
                    
                #self.region_candidates = None
                #self.candidates = None
                #self.candidates_triangles = None
                #print(f"Pas assez de triangles candidats pour l'expansion (seulement {len(region)} trouvés).")
                return
            else:
                self.region_candidates+=region
                # Fusionner les doublons dans self.region_candidates
                self.region_candidates = list(set(self.region_candidates))
        elif type == "expansion_empty":
            if len(region) < nb_min_region or density > min_density or max_edge > 3 or perimeter*perimeter>ratio_area*4*3.14*total_area or len(border_edges)<7:
                #self.region_empty = None
                #self.empty_triangles = None
                #print(f"Pas assez de triangles vides pour l'expansion vide (seulement {len(region)} trouvés).")
                if False:
                    if perimeter*perimeter>ratio_area*4*3.14*total_area:
                        print(f"inegalité : {perimeter*perimeter:.2f} > {ratio_area}*4*3.14*{total_area:.2f} = {ratio_area*4*3.14*total_area:.2f}")
                    if len(border_edges)<7:
                        print(f"Pas assez de bords pour l'expansion vide (seulement {len(border_edges)} trouvés).")
                    if density > min_density:
                        print(f"Densité trop élevée pour l'expansion vide : {density:.2f}, min : {min_density} (périmètre : {perimeter:.2f}, nombre de bords : {len(border_edges)})")
                    if max_edge > 3:
                        print(f"Expansion vide rejetée car le côté maximal {max_edge:.2f} est supérieur à 3.")
                    if len(region) < nb_min_region:
                        print(f"Pas assez de triangles vides pour l'expansion vide (seulement {len(region)} trouvés).")
            else:
                self.region_empty += region
                # Fusionner les doublons dans self.region_empty
                self.region_empty = list(set(self.region_empty))
        #if len(region) < nb_min_region:print(f"Pas assez de triangles pour l'expansion {type} (seulement {len(region)} trouvés).")
        #if density>min_density:print(f"Densité trop élevée pour l'expansion {type} : {density:.2f}, min : {min_density} (périmètre : {perimeter:.2f}, nombre de bords : {len(border_edges)})")
        #if max_edge > 2:print(f"Expansion {type} rejetée car le côté maximal {max_edge:.2f} est supérieur à 2.")
            
        return
    
    def expansion_candidates(self, ratio_threshold=1.3,min_density=1.5, nb_min_region=4, ratio_area=1.4):
        if self.candidates_triangles is None or self.points is None or self.tri is None or self.candidates is None:
                self.region_candidates = None
                return None
        self.region_candidates = []
        print(f"Début de l'expansion candidates avec {self.candidates} candidats.")
        for triangles in self.candidates_triangles:
            self.expansion(triangles, "expansion_candidate", ratio_threshold,min_density, nb_min_region, ratio_area)
        
        
    def expansion_empty(self, ratio_threshold=1.3, min_density=1.5, nb_min_region=4, ratio_area=1.4):
        if self.empty_triangles is None or self.points is None or self.tri is None:
                self.region_empty = None
                return None
        self.region_empty = []
        print(f"Début de l'expansion vide avec {len(self.empty_triangles)} triangles vides.")
        for triangles in self.empty_triangles:
            self.expansion(triangles, "expansion_empty", ratio_threshold, min_density, nb_min_region, ratio_area)
     