import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.widgets import Button

def icosahedron_vertices():
    phi = (1 + np.sqrt(5)) / 2
    vertices = np.array([
        [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
        [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
        [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
    ])

    return vertices / np.linalg.norm(vertices[0])

def icosahedron_faces():
    return np.array([
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
    ])

def plot_icosahedron():
    vertices = icosahedron_vertices()
    faces = icosahedron_faces()

    fig = plt.figure()
    fig.canvas.manager.set_window_title("Лабораторная работа №5. Икосаэдр")
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        triangle = vertices[face]
        poly = art3d.Poly3DCollection([triangle], facecolors='#C6F4D6', edgecolors='k', linewidths=1, alpha=0.9)
        ax.add_collection3d(poly)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='k', s=50)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')

    ax.view_init(elev=10, azim=30)

    plt.show()

plot_icosahedron()
