"""
napari conversion utilities for PySNT.

Functions to convert SNT Tree objects into the array formats expected by
napari layers (Shapes, Points, Surface). They only depend on numpy: napari
itself is never imported, so the functions can be used (and tested) without it.

Coordinate conventions
----------------------
napari uses (z, y, x) ordering, whereas SNT uses (x, y, z). All arrays returned
here are in (z, y, x) order and in SNT's spatial units (typically um). When
overlaying a reconstruction on an image, set the image layer's ``scale`` to the
image calibration (voxel size in (z, y, x) order) so that both share a space.
"""

import logging
from typing import Tuple

import numpy as np

logger = logging.getLogger(__name__)

# Fallback vertex color for nodes without an assigned color (RGBA, 0-1)
_DEFAULT_RGBA = (0.5, 0.5, 0.5, 1.0)


def _iter_paths(tree):
    """Yield the Paths of a Tree."""
    return tree.list()


def _node_zyx(node) -> Tuple[float, float, float]:
    """Return the coordinates of a node in napari's (z, y, x) order."""
    return node.z, node.y, node.x


def _color_to_rgba(color) -> Tuple[float, float, float, float]:
    """Convert a java.awt.Color (or None) to an RGBA tuple in the 0-1 range."""
    if color is None:
        return _DEFAULT_RGBA
    return (
        color.getRed() / 255.0,
        color.getGreen() / 255.0,
        color.getBlue() / 255.0,
        color.getAlpha() / 255.0,
    )


def tree_to_napari_paths(tree) -> list:
    """
    Convert the Paths of a Tree to polylines for a napari Shapes layer.

    Parameters
    ----------
    tree : Tree
        PySNT Tree object

    Returns
    -------
    list of np.ndarray
        One (N, 3) array of (z, y, x) coordinates per Path. Paths with fewer
        than two nodes are skipped.

    Examples
    --------
    >>> from pysnt.converters import tree_to_napari_paths
    >>> paths = tree_to_napari_paths(tree)
    >>> viewer.add_shapes(paths, shape_type='path', edge_width=1)
    """
    paths = []
    for path in _iter_paths(tree):
        n = path.size()
        if n < 2:
            continue
        paths.append(np.array([_node_zyx(path.getNode(i)) for i in range(n)], dtype=float))
    return paths


def tree_to_napari_points(tree, valid_only: bool = True) -> Tuple[np.ndarray, np.ndarray]:
    """
    Convert the nodes of a Tree to points with radii for a napari Points layer.

    Parameters
    ----------
    tree : Tree
        PySNT Tree object
    valid_only : bool, default True
        Discard nodes without a valid radius (non-finite or not larger than
        zero). Reconstructions without radii yield empty arrays in this case.

    Returns
    -------
    coords : np.ndarray
        (N, 3) array of (z, y, x) coordinates
    radii : np.ndarray
        (N,) array of node radii

    Examples
    --------
    >>> from pysnt.converters import tree_to_napari_points
    >>> coords, radii = tree_to_napari_points(tree)
    >>> viewer.add_points(coords, size=2 * radii, features={'radius': radii},
    ...                   face_color='radius', face_colormap='viridis')
    """
    coords, radii = [], []
    for path in _iter_paths(tree):
        for i in range(path.size()):
            node = path.getNode(i)
            coords.append(_node_zyx(node))
            radii.append(node.radius)
    coords = np.array(coords, dtype=float).reshape(-1, 3)
    radii = np.array(radii, dtype=float)
    if valid_only:
        mask = np.isfinite(radii) & (radii > 0)
        coords, radii = coords[mask], radii[mask]
    return coords, radii


def tree_to_napari_surface(
    tree, n_sides: int = 8, colors: bool = False, min_radius: float = 0.0
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Convert a Tree to a surface mesh for a napari Surface layer.

    Each segment between consecutive nodes is rendered as a truncated cone
    (frustum) whose end radii match the node radii, so that local thickness is
    represented accurately.

    Parameters
    ----------
    tree : Tree
        PySNT Tree object
    n_sides : int, default 8
        Number of sides of each frustum. Higher values yield smoother meshes
        at the cost of memory.
    colors : bool, default False
        If False, per-vertex values are node radii (for use with a napari
        colormap). If True, per-vertex values are RGBA colors taken from the
        nodes (e.g., after mapping a metric with ``TreeColorMapper``) and
        should be assigned to ``layer.vertex_colors``.
    min_radius : float, default 0.0
        Lower bound for node radii. Use a small positive value to render
        reconstructions that lack radii (which would otherwise be invisible).

    Returns
    -------
    vertices : np.ndarray
        (V, 3) array of (z, y, x) vertex coordinates
    faces : np.ndarray
        (F, 3) array of vertex indices
    values : np.ndarray
        (V,) array of radii, or (V, 4) array of RGBA colors if ``colors``
        is True

    Raises
    ------
    ValueError
        If the Tree has no segments of non-zero length

    Examples
    --------
    >>> from pysnt.converters import tree_to_napari_surface
    >>> vertices, faces, radii = tree_to_napari_surface(tree)
    >>> viewer.add_surface((vertices, faces, radii), colormap='viridis')

    >>> # Color-code by a mapped metric
    >>> TreeColorMapper().map(tree, 'distance to soma', 'viridis')
    >>> vertices, faces, rgba = tree_to_napari_surface(tree, colors=True)
    >>> layer = viewer.add_surface((vertices, faces))
    >>> layer.vertex_colors = rgba
    """
    if n_sides < 3:
        raise ValueError("n_sides must be at least 3")

    p1, p2, r1, r2, c1, c2 = [], [], [], [], [], []
    for path in _iter_paths(tree):
        nodes = [path.getNode(i) for i in range(path.size())]
        for a, b in zip(nodes[:-1], nodes[1:]):
            p1.append(_node_zyx(a))
            p2.append(_node_zyx(b))
            r1.append(a.radius)
            r2.append(b.radius)
            if colors:
                c1.append(_color_to_rgba(a.getColor()))
                c2.append(_color_to_rgba(b.getColor()))

    if not p1:
        raise ValueError("Tree has no segments to render")

    p1 = np.array(p1, dtype=float)
    p2 = np.array(p2, dtype=float)
    r1 = np.nan_to_num(np.array(r1, dtype=float), nan=0.0, posinf=0.0, neginf=0.0)
    r2 = np.nan_to_num(np.array(r2, dtype=float), nan=0.0, posinf=0.0, neginf=0.0)
    r1 = np.maximum(r1, min_radius)
    r2 = np.maximum(r2, min_radius)

    # Discard zero-length segments (no defined axis)
    direction = p2 - p1
    length = np.linalg.norm(direction, axis=1)
    keep = length > 0
    if not keep.any():
        raise ValueError("Tree has no segments of non-zero length")
    p1, p2, r1, r2 = p1[keep], p2[keep], r1[keep], r2[keep]
    direction = direction[keep] / length[keep, None]
    if colors:
        c1 = np.array(c1, dtype=float)[keep]
        c2 = np.array(c2, dtype=float)[keep]

    # Orthonormal frame perpendicular to each segment (components in z, y, x)
    ref = np.where(
        (np.abs(direction[:, 0]) < 0.9)[:, None], [[1.0, 0.0, 0.0]], [[0.0, 0.0, 1.0]]
    )
    perp1 = np.cross(direction, ref)
    perp1 /= np.linalg.norm(perp1, axis=1, keepdims=True)
    perp2 = np.cross(direction, perp1)

    # Rings of n_sides vertices at both ends of every segment: (S, 2 * n_sides, 3)
    angles = np.linspace(0.0, 2.0 * np.pi, n_sides, endpoint=False)
    ring = (np.cos(angles)[None, :, None] * perp1[:, None, :]
            + np.sin(angles)[None, :, None] * perp2[:, None, :])
    ring1 = p1[:, None, :] + r1[:, None, None] * ring
    ring2 = p2[:, None, :] + r2[:, None, None] * ring
    n_seg = len(p1)
    vertices = np.concatenate([ring1, ring2], axis=1).reshape(-1, 3)

    # Two triangles per side, joining the rings
    i = np.arange(n_sides)
    j = (i + 1) % n_sides
    template = np.concatenate([
        np.stack([i, j, i + n_sides], axis=1),
        np.stack([j, j + n_sides, i + n_sides], axis=1),
    ])
    offsets = (np.arange(n_seg) * 2 * n_sides)[:, None, None]
    faces = (template[None, :, :] + offsets).reshape(-1, 3)

    if colors:
        values = np.concatenate([
            np.repeat(c1[:, None, :], n_sides, axis=1),
            np.repeat(c2[:, None, :], n_sides, axis=1),
        ], axis=1).reshape(-1, 4)
    else:
        values = np.concatenate([
            np.repeat(r1[:, None], n_sides, axis=1),
            np.repeat(r2[:, None], n_sides, axis=1),
        ], axis=1).reshape(-1)

    return vertices, faces, values
