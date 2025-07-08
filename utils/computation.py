import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import Voronoi
from collections import defaultdict

class Computation():
    def __init__(self):
        self.points = None
        self.tri = None
        self.triangle_counts = None
        self.areas = None
        self.candidates = None
        self.empty_triangles = None

    def afficher(self, id_to_track, candidates, message):
        if not all(x in candidates for x in id_to_track): #inclusion
            lost_ids = [id for id in id_to_track if id not in candidates]
            print("Perte de candidats : ", message, " : ", lost_ids)
            return [id for id in id_to_track if id in candidates]
        return id_to_track

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
        points_a_exclure = [8]
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
        if not np.array_equal(self.points, points):
            self.points = points
             
        if self.tri != tri:
            self.tri = tri
             
        if self.triangle_counts != triangle_counts:
            self.triangle_counts = triangle_counts
             
        if self.areas != areas:
            self.areas = areas
             
        
        return None

    def personnes_centrales(self, n_triangles, distance_min, angle_max, id_to_track=[]):
        points = self.points
        tri = self.tri
        triangle_counts = self.triangle_counts
        areas = self.areas

        if tri is None or triangle_counts is None:
            return None
        candidates = {idx: count for idx, count in triangle_counts.items() if areas.get(idx, np.inf) != np.inf}
        id_to_track = self.afficher(id_to_track, candidates, "aire infinie")
        if not candidates:
            return None
        candidates = {idx: count for idx, count in candidates.items() if count >= n_triangles}
        id_to_track = self.afficher(id_to_track, candidates, f"moins de {n_triangles} triangles")
        if not candidates:
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
            return None
        if len(filtered_candidates) == 1:
            if self.candidates != filtered_candidates:
                self.candidates = filtered_candidates
                return filtered_candidates
            return None
        non_candidate_neighbors = []
        for idx in filtered_candidates:
            point = points[idx]
            for other_idx, other_point in enumerate(points):
                if other_idx not in filtered_candidates:
                    if other_idx not in non_candidate_neighbors:
                        non_candidate_neighbors.append(other_idx)
        final_candidates = []
        for idx in filtered_candidates:
            angles = []
            point = points[idx]
            for other_idx in non_candidate_neighbors:
                other_point = points[other_idx]
                vector = other_point - point
                angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi + 180
                angles.append(angle)
            angles = np.sort(np.array(angles))
            differences = np.diff(angles)
            if max(differences) < angle_max and 360 + angles[0] - angles[-1] < angle_max:
                final_candidates.append(idx)
        id_to_track = self.afficher(id_to_track, final_candidates, f"angle max {angle_max}°")
        if self.candidates != final_candidates:
            self.candidates = final_candidates
            return final_candidates if final_candidates else None
        return None

    def empty_zones(self, area_threshold=4):
        points = self.points
        tri = self.tri
        if tri is None or points is None:
            return None
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
        if self.empty_triangles != empty_triangles:
            self.empty_triangles = empty_triangles
            return empty_triangles
        return None

    def edge_length(self, p1, p2):
        return np.linalg.norm(p1 - p2)

    def get_edge_indices(self, triangle):
        return [(triangle[0], triangle[1]),
                (triangle[1], triangle[2]),
                (triangle[2], triangle[0])]

    def expansion(self, triangles, tri, points, ratio_threshold=1.5):
        if tri is None or points is None or triangles is None:
            return None
        region = set(triangles.index())
        visited = set()
        to_visit = list(region)
        while to_visit:
            current_idx = to_visit.pop()
            visited.add(current_idx)
            current_triangle = tri.simplices[current_idx]
            for i, neighbor_idx in enumerate(tri.neighbors[current_idx]):
                if neighbor_idx == -1 or neighbor_idx in visited or neighbor_idx in region:
                    continue
                neighbor_triangle = tri.simplices[neighbor_idx]
                shared = set(current_triangle) & set(neighbor_triangle)
                if len(shared) != 2:
                    continue
                a, b = list(shared)
                edge = self.edge_length(points[a], points[b])
                other_points = list(set(neighbor_triangle) - shared)
                if len(other_points) != 1:
                    continue
                c = other_points[0]
                d1 = self.edge_length(points[a], points[c])
                d2 = self.edge_length(points[b], points[c])
                if d1 + d2 < ratio_threshold * edge:
                    region.add(neighbor_idx)
                    to_visit.append(neighbor_idx)
        # Pas de variable de classe à mettre à jour ici (pas de self.region)
        return