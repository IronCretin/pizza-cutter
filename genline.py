"""
Various methods to generate lines.
All return an pair of two points defining line.
TODO: define rest of functions
"""
from math import pi, sqrt, cos, sin
import random as rnd
from typing import Tuple, Sequence


Point = Tuple[float, float]
Line = Tuple[Point, Point]


def mag(pt: Sequence[float]) -> float:
    return sqrt(sum(x**2 for x in pt))


def gen_point() -> Point:
    """
    Generates a random point inside the circle.
    """
    while True:  # Try until a point is inside the circle
        coords = rnd.uniform(-1, 1), rnd.uniform(-1, 1)  # Pick x, y
        if mag(coords) < 1:  # Verify they're inside the circle
            return coords


def edge_point() -> Point:
    """
    Generates a random point on the circle's circumference.
    """
    t = rnd.uniform(0, 2*pi)  # Choose a random angle
    return cos(t), sin(t)  # Return the point at that angle on the circle


def edge_points() -> Line:
    """
    Pick two points on the edge, draw a line between them.
    """
    return edge_point(), edge_point()


def two_points() -> Line:
    """
    Pick two random points inside circle.
    """
    return gen_point(), gen_point()

def point_angle() -> Line:
    """
    Pick a point, pick an angle for the line.
    """
    ...

def point_chord() -> Line:
    """
    Pick a point, draw the chord with it as the midpoint.
    """
    ...

def bisect_chord() -> Line:
    """
    Pick a bisecting line, pick a point on it, draw the chord with it as the
    midpoint.
    """
    ...
