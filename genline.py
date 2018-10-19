import numpy as np
from math import *


def gen_point():
    while True:
        p = np.random.uniform(-.5, .5, 2)
        if np.linalg.norm(p) < .5:
            return p

def two_points():
    ...

def point_angle():
    ...

def point_chord():
    ...

def edge_angle():
    ...
