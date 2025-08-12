import numpy as np
from sympy import Eq
from sympy.abc import V, E, F

def get_solid(name):
    """
    Returns vertices and faces for the given Platonic solid.
    """
    if name == "Tetrahedron":
        vertices = np.array([
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, -1],
            [1, -1, -1]
        ])
        faces = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]

    elif name == "Cube":
        vertices = np.array([
            [-1, -1, -1], [1, -1, -1],
            [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1],
            [1, 1, 1], [-1, 1, 1]
        ])
        faces = [
            [0,1,2,3], [4,5,6,7],
            [0,1,5,4], [2,3,7,6],
            [1,2,6,5], [0,3,7,4]
        ]

    elif name == "Octahedron":
        vertices = np.array([
            [1,0,0], [-1,0,0],
            [0,1,0], [0,-1,0],
            [0,0,1], [0,0,-1]
        ])
        faces = [
            [0,2,4], [2,1,4], [1,3,4], [3,0,4],
            [0,2,5], [2,1,5], [1,3,5], [3,0,5]
        ]

    elif name == "Dodecahedron":
        from scipy.spatial import ConvexHull
        phi = (1 + np.sqrt(5)) / 2
        a, b = 1, 1 / phi
        points = []
        for i in [-a, a]:
            for j in [-a, a]:
                for k in [-a, a]:
                    points.append([i, j, k])
        for i in [-b, b]:
            for j in [-b, b]:
                points += [[0, i, j], [i, 0, j], [i, j, 0]]
        vertices = np.array(points)
        hull = ConvexHull(vertices)
        faces = hull.simplices.tolist()

    else:
        return None, None

    return vertices, faces

def symbolic_description(name):
    """
    Returns Euler's formula and symbolic counts for the solid.
    """
    if name == "Tetrahedron":
        return Eq(V - E + F, 2), {"V": 4, "E": 6, "F": 4}
    elif name == "Cube":
        return Eq(V - E + F, 2), {"V": 8, "E": 12, "F": 6}
    elif name == "Octahedron":
        return Eq(V - E + F, 2), {"V": 6, "E": 12, "F": 8}
    elif name == "Dodecahedron":
        return Eq(V - E + F, 2), {"V": 20, "E": 30, "F": 12}
    else:
        return None, {}

def get_symbolic_overlay(name):
    """
    Placeholder for symbolic overlays (e.g. Metatron’s Cube, golden spirals).
    """
    overlays = {
        "Tetrahedron": "Fire, initiation, upward motion",
        "Cube": "Earth, stability, foundation",
        "Octahedron": "Air, balance, duality",
        "Dodecahedron": "Ether, cosmos, divine geometry"
    }
    return overlays.get(name, "No symbolic overlay defined.")

# Optional: UI selector (if needed)
def select_solid():
    import streamlit as st
    return st.sidebar.selectbox("Choose a Platonic Solid", ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron"])
