import numpy as np
from scipy.spatial import Delaunay

def triangles(positions, width, height):
    """On prend en entrée un dictionnaire avec les positions des objets détectés"""
    # On extrait les points des positions
    points = np.array([pos for pos in positions.values() if pos is not None])
    # On exclut les points qui sont en dehors de la scène
    points = points[(points[:, 0] >= 0) & (points[:, 0] <= width) & 
                    (points[:, 1] >= 0) & (points[:, 1] <= height)]

    # On s'assure que les points sont uniques
    points = np.unique(points, axis=0)

    # Si moins de 3 points uniques, on ne peut pas faire de triangulation
    if len(points) < 3:
        print(f"\rPas assez de points uniques pour la triangulation.", end="")
        return None, None
    # Triangulation de Delaunay
    tri = Delaunay(points)
    return points,tri
