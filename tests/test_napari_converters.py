"""Tests for the napari converters (numpy only: neither napari nor Java is required)."""

import numpy as np
import pytest

from pysnt.converters import (
    tree_to_napari_paths,
    tree_to_napari_points,
    tree_to_napari_surface,
)


class _Color:
    def __init__(self, r, g, b, a=255):
        self._v = (r, g, b, a)

    def getRed(self):
        return self._v[0]

    def getGreen(self):
        return self._v[1]

    def getBlue(self):
        return self._v[2]

    def getAlpha(self):
        return self._v[3]


class _Node:
    def __init__(self, x, y, z, radius, color=None):
        self.x, self.y, self.z, self.radius, self._color = x, y, z, radius, color

    def getColor(self):
        return self._color


class _Path:
    def __init__(self, nodes):
        self._nodes = nodes

    def size(self):
        return len(self._nodes)

    def getNode(self, i):
        return self._nodes[i]


class _Tree:
    def __init__(self, paths):
        self._paths = paths

    def list(self):
        return self._paths


@pytest.fixture
def tree():
    red = _Color(255, 0, 0)
    return _Tree([
        _Path([_Node(0, 0, 0, 1, red), _Node(10, 0, 0, 2), _Node(10, 10, 0, 3, red)]),
        _Path([_Node(1, 1, 1, 0)]),  # single node
        _Path([_Node(5, 5, 5, float("nan")), _Node(5, 5, 5, 1)]),  # zero-length
        _Path([_Node(0, 0, 0, 1), _Node(0, 0, 10, 1)]),
    ])


def test_paths_are_zyx_and_skip_single_nodes(tree):
    paths = tree_to_napari_paths(tree)
    assert len(paths) == 3
    # node (x=10, y=0, z=0) is (z, y, x) = (0, 0, 10)
    np.testing.assert_array_equal(paths[0][1], [0, 0, 10])


def test_points_filter_invalid_radii(tree):
    coords, radii = tree_to_napari_points(tree)
    assert coords.shape == (len(radii), 3) and np.all(radii > 0)
    all_coords, _ = tree_to_napari_points(tree, valid_only=False)
    assert len(all_coords) == 8


def test_surface_geometry(tree):
    n = 8
    vertices, faces, radii = tree_to_napari_surface(tree, n_sides=n)
    # 3 segments with non-zero length
    assert vertices.shape == (3 * 2 * n, 3)
    assert faces.shape == (3 * 2 * n, 3)
    assert radii.shape == (len(vertices),)
    assert faces.max() < len(vertices)
    # first segment runs along x: ring at the origin has radius 1, x == 0
    ring = vertices[:n]
    np.testing.assert_allclose(np.linalg.norm(ring, axis=1), 1)
    np.testing.assert_allclose(ring[:, 2], 0, atol=1e-12)


def test_surface_vertex_colors_and_min_radius(tree):
    _, _, rgba = tree_to_napari_surface(tree, colors=True)
    assert rgba.shape[1] == 4
    np.testing.assert_allclose(rgba[0], [1, 0, 0, 1])  # colored node
    np.testing.assert_allclose(rgba[8], [0.5, 0.5, 0.5, 1])  # default gray
    _, _, radii = tree_to_napari_surface(tree, min_radius=0.5)
    assert radii.min() >= 0.5


def test_surface_errors():
    with pytest.raises(ValueError):
        tree_to_napari_surface(_Tree([_Path([_Node(0, 0, 0, 1)])]))
    with pytest.raises(ValueError):
        tree_to_napari_surface(_Tree([_Path([_Node(0, 0, 0, 1), _Node(1, 0, 0, 1)])]), n_sides=2)
