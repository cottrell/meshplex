import numpy as np

import meshplex


def test_mesh_line():
    pts = [0.0, 1.0, 3.0, 4.0]
    cells = [[0, 1], [1, 2], [2, 3]]
    mesh = meshplex.MeshLine(pts, cells)
    print(mesh.cell_volumes)
    ref = [1.0, 2.0, 1.0]
    assert np.all(np.abs(mesh.cell_volumes - ref) < np.abs(ref) * 1.0e-13)


def test_vol_tri():
    # two triangles in 5D
    points = [
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0],
    ]
    cells = [[0, 1, 2], [0, 3, 2]]
    mesh = meshplex.Mesh(points, cells)

    ref = [0.5, 0.5]
    print(mesh.cell_volumes)
    assert np.all(np.abs(mesh.cell_volumes - ref) < np.abs(ref) * 1.0e-13)


def test_vol_tetra():
    points = [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
    cells = [[0, 1, 2, 3]]
    mesh = meshplex.Mesh(points, cells)

    ref = [1 / 6]
    print(mesh.cell_volumes)
    assert np.all(np.abs(mesh.cell_volumes - ref) < np.abs(ref) * 1.0e-13)


def test_vol_simplex5():
    points = [
        [0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    cells = [[0, 1, 2, 3, 4]]
    mesh = meshplex.Mesh(points, cells)

    ref = [1 / 24]
    print(mesh.cell_volumes)
    assert np.all(np.abs(mesh.cell_volumes - ref) < np.abs(ref) * 1.0e-13)


if __name__ == "__main__":
    # test_vol_tri()
    test_vol_tetra()
