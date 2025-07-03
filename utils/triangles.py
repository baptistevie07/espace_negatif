import numpy as np
from scipy.spatial import Delaunay

def triangles(positions):
    """On prend en entrée un dictionnaire avec les positions des objets détectés"""
    # On extrait les points des positions
    points = np.array([pos for pos in positions.values() if pos is not None])

    # On s'assure que les points sont uniques
    points = np.unique(points, axis=0)

    # Si moins de 3 points uniques, on ne peut pas faire de triangulation
    if len(points) < 3:
        print("Pas assez de points uniques pour la triangulation.")
        return None, None
    # Triangulation de Delaunay
    tri = Delaunay(points)

    return points,tri
