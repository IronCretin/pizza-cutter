"""
Various methods to generate lines
All return an array of two points defining line
TODO: define rest of functions
"""
import numpy as np
from math import pi


def gen_point():
    """
    Generates a random point in the circle
    """
    while True:
        p = np.random.uniform(-1, 1, 2)
        if np.linalg.norm(p) < 1:
            return p

def edge_points():
    """
    Pick two points on the edge, draw a line between them
    """
    t = np.random.uniform(0, 2*pi, 2)
    return np.vstack([np.cos(t), np.sin(t)]).T

def two_points():
    """
    Pick two random points inside circle
    """
    ...

def point_angle():
    """
    Pick a point, pick an angle for the line
    """
    ...

def point_chord():
    """
    Pick a point, draw a chord through it
    """
    ...

def bisect_chord():
    """
    Pick a bisecting line, pick a point on it, draw a chord through it
    """
    ...
