import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import Voronoi
from collections import defaultdict

def computation(positions,ages, width, height):
    """On prend en entrée un dictionnaire avec les positions des objets détectés"""
    # On extrait les points des positions
    points = np.array([pos for pos in positions.values() if pos is not None])
    ages = np.array([ages[obj] for obj in positions.keys() if positions[obj] is not None])
    if len(points) < 3:
        print(f"\rPas assez de points uniques pour la triangulation (avant filtrage).", end="")
        return None, None, None, None
    # On exclut les points qui sont en dehors de la scène
    mask=((points[:, 0] >= 0) & (points[:, 0] <= width) & 
                    (points[:, 1] >= 0) & (points[:, 1] <= height)&(ages>30))
    points = points[mask]
    # On s'assure que les points sont uniques
    points = np.unique(points, axis=0)

    # Si moins de 3 points uniques, on ne peut pas faire de triangulation
    if len(points) < 3:
        print(f"\rPas assez de points uniques pour la triangulation (après filtrage).", end="")
        return None, None, None, None
    # Triangulation de Delaunay
    tri = Delaunay(points)

    
    triangle_counts = defaultdict(int)

    for simplex in tri.simplices:
        for vertex in simplex:
            triangle_counts[vertex] += 1

    # Voronoï diagram
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
            areas[idx] = np.inf  # Cellule infinie → point au bord

    return points,tri,triangle_counts,areas

def personnes_centrales(points,tri, triangle_counts,areas,n_triangles,distance_min,angle_max):
    """Cherche les candidats qui puissent être au centre des zones"""
    if tri is None or triangle_counts is None:
        return None
    # On ne conserve que les candidats à l'aire non infinie
    candidates = {idx: count for idx, count in triangle_counts.items() if areas.get(idx, np.inf) != np.inf}
    if not candidates:
        return None
    # On garde uniquement les candidats avec plus de n_triangles triangles
    candidates = {idx: count for idx, count in candidates.items() if count >= n_triangles}
    if not candidates:
        return None
    # Parmi les candidats restants, on enlève ceux qui sont proches d'un autre point (dans points) qui n'est pas candidat
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
    if len(filtered_candidates) == 0:
        return None
    # Si on a un seul candidat, on le retourne
    if len(filtered_candidates) == 1:
        return filtered_candidates
    # S'il reste plusieurs candidats, on vérifie qu'il n'y a pas de faux positifs parmis eux. 
    # D'abord on liste tous les points non candidats, voisins de candidats
    non_candidate_neighbors = []
    for idx in filtered_candidates:
        point = points[idx]
        for other_idx, other_point in enumerate(points):
            if other_idx not in filtered_candidates:
                if other_idx not in non_candidate_neighbors:
                    non_candidate_neighbors.append(other_idx)
    # On calcule les angles des vecteurs candidats - voisins non candidats
    #print(f"Nombre de candidats après filtrage : {len(filtered_candidates)}")
    final_candidates = []
    #print(f"Nombre de candidats après filtrage : {len(filtered_candidates)}")
    #print(f"Nombre de voisins non candidats : {len(non_candidate_neighbors)}")
    for idx in filtered_candidates:
        #print(f"Vérification des angles pour le candidat {idx}")
        angles = []
        point = points[idx]
        for other_idx in non_candidate_neighbors:
            other_point = points[other_idx]
            vector = other_point - point
            angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi+180
            angles.append(angle)
        angles = np.sort(np.array(angles))
        #print(f"Angles pour le candidat {idx}: {angles}")
        differences = np.diff(angles)
        # On vérifie si l'angle minimum est respecté
        #print(f"Angle max pour le candidat {idx}: {max(differences)}")
        if max(differences) < angle_max and 360 + angles[0] - angles[-1] < angle_max: #cas où le dernier angle est proche du premier
            final_candidates.append(idx)
    
    #print(f"Nombre de candidats après vérification des angles : {len(filtered_candidates)}")


    return final_candidates if final_candidates else None
