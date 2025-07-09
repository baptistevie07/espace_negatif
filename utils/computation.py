import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import Voronoi
from scipy.spatial import cKDTree
from collections import defaultdict
import time

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

    def afficher(self, id_to_track, candidates, message):
        if not all(x in candidates for x in id_to_track): #inclusion
            lost_ids = [id for id in id_to_track if id not in candidates]
            print("Perte de candidats : ", message, " : ", lost_ids)
            return [id for id in id_to_track if id in candidates]
        return id_to_track
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

    def computation(self, positions, ages, width, height):
        points = np.array([pos for pos in positions.values() if pos is not None])
        ages = np.array([ages[obj] for obj in positions.keys() if positions[obj] is not None])
        if len(points) < 3:
            print(f"\rPas assez de points uniques pour la triangulation (avant filtrage).", end="")
            return None
        mask = ((points[:, 0] >= 0) & (points[:, 0] <= width) &
                (points[:, 1] >= 0) & (points[:, 1] <= height) & (ages > 30))
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
        #print(f"Triangulation Delaunay effectuée avec {len(tri.simplices)} triangles.")
             
        
        self.triangle_counts = triangle_counts
             
        
        self.areas = areas
             
        
        return None

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
        candidates = {idx: count for idx, count in triangle_counts.items() if areas.get(idx, np.inf) != np.inf}
        id_to_track = self.afficher(id_to_track, candidates, "aire infinie")
        if not candidates:
            self.candidates = None
            self.candidates_triangles = None
            return None
        candidates = {idx: count for idx, count in candidates.items() if count >= n_triangles}
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
        non_candidate_neighbors = []
        for idx in filtered_candidates:
            point = points[idx]
            for other_idx, other_point in enumerate(points):
                if other_idx not in filtered_candidates:
                    if other_idx not in non_candidate_neighbors:
                        non_candidate_neighbors.append(other_idx)
        final_candidates = []

        for idx in filtered_candidates:
            point = points[idx]
            angles = []
            vectors = []
            other_indices = []

            for other_idx in non_candidate_neighbors:
                other_point = points[other_idx]
                vector = other_point - point
                angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi + 180
                angles.append(angle)
                vectors.append(vector)
                other_indices.append(other_idx)

            if len(angles) < 2:
                continue  # impossible de former un angle

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
                if delta > 120:
                    keep = False
                    if idx in id_to_track:
                        print(f"Point {idx} rejeté pour angle trop grand {delta:.1f}°")
                    break
                # Grands angles suspects → tester si géométriquement "fermés"
                a_idx = sorted_neighbors[i]
                b_idx = sorted_neighbors[(i + 1) % len(sorted_neighbors)]

                d_ab = np.linalg.norm(points[a_idx] - points[b_idx])
                d_ai = np.linalg.norm(points[a_idx] - point)
                d_bi = np.linalg.norm(points[b_idx] - point)

                # Tolérance souple (ex : 90% de la distance AB)
                if not (d_ai < 0.9 * d_ab and d_bi < 0.9 * d_ab):
                    keep = False
                    if idx in id_to_track:
                        print(f"Point {idx} rejeté pour angle suspect {delta:.1f}° entre {a_idx} et {b_idx}")
                    break  # au moins un grand angle non tolérable → rejet

            if keep:
                final_candidates.append(idx)

        id_to_track = self.afficher(id_to_track, final_candidates, f"angle max {angle_max}°")

        delaunay_neighbors = self.build_delaunay_neighbors(tri)
        final2_candidates = []
        for idx in final_candidates:
            if self.has_distant_delaunay_neighbors(idx, points, delaunay_neighbors, min_dist=1.5, min_count=2):
                final2_candidates.append(idx)
        id_to_track = self.afficher(id_to_track, final2_candidates, f"voisins éloignés (distance >= 2.0)")

        
        candidates_triangles = {}
        idx=0
        for simplex in self.tri.simplices:
            if any(vertex in final2_candidates for vertex in simplex):
                candidates_triangles[idx] = simplex.tolist()
            idx+=1
        
        self.candidates = final2_candidates
        
        self.candidates_triangles = candidates_triangles
        #print(candidates_triangles)
        #print("Nombre total de triangles", len(tri.simplices))
        #print(f"Personnes centrales trouvées : {final_candidates}")
        return None

    def empty_zones(self, area_threshold=4, radius=1):
        
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
        #print(f"triangles vides trouvés : {empty_triangles}")
        # Parmis ces candidats, on va vérifier que tous les sommets ont au moins 2 voisins proches
        #print(f"Nombre de triangles vides trouvés : {len(empty_triangles)}")
        if not empty_triangles or self.tree== None:
            self.empty_triangles = None
            return None
        filtered_empty_triangles = {}
        
        for id,triangle in empty_triangles.items():
            potentiel = True
            for i in triangle:
                # Chercher tous les points dans le rayon autour du sommet
                neighbor_ids = self.tree.query_ball_point(points[i], r=radius)
                
                valid_neighbors = [nid for nid in neighbor_ids if nid != i]
                
                if len(valid_neighbors) < 2: #Au moins deux voisins proches
                    potentiel = False
            if potentiel:
                filtered_empty_triangles[id] = triangle
            
        if not filtered_empty_triangles:
            self.empty_triangles = None           
        self.empty_triangles = filtered_empty_triangles
        #print(f"Nombre de triangles vides filtrés : {len(self.empty_triangles)}")
        if len(self.empty_triangles) == 0:
            self.empty_triangles = None
            return None
        return None

    def edge_length(self, p1, p2):
        return np.linalg.norm(p1 - p2)

    def get_edge_indices(self, triangle):
        return [(triangle[0], triangle[1]),
                (triangle[1], triangle[2]),
                (triangle[2], triangle[0])]

    def expansion(self, type,ratio_threshold,nb_min_region=4):
        
        #nb_iterations = int(time.time())% 20 
        if type=="expansion_candidate":
            if self.candidates_triangles is None or self.points is None or self.tri is None:
                self.region_candidates = None
                return None

            triangles = self.candidates_triangles
        elif type=="expansion_empty":
            if self.empty_triangles is None or self.points is None or self.tri is None:
                self.region_empty = None
                return None
            triangles = self.empty_triangles
        else:
            print(f"Type '{type}' non reconnu pour expansion.")
            return None
        #print(f"debut expansion de type {type} avec {len(self.tri.simplices)} triangles")
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
        if type == "expansion_candidate":
            if len(region) < nb_min_region:
                self.region_candidates = None
                self.candidates = None
                self.candidates_triangles = None
                #print(f"Pas assez de triangles candidats pour l'expansion (seulement {len(region)} trouvés).")
            else:
                self.region_candidates = region
        elif type == "expansion_empty":
            if len(region) < nb_min_region:
                self.region_empty = None
                self.empty_triangles = None
                #print(f"Pas assez de triangles vides pour l'expansion vide (seulement {len(region)} trouvés).")
            else:
                self.region_empty = region
        return
    
    def expansion_candidates(self, ratio_threshold=1.3):
        self.expansion("expansion_candidate", ratio_threshold)
    def expansion_empty(self, ratio_threshold=1.3):
        self.expansion("expansion_empty", ratio_threshold)