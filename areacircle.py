from math import pi
import sys


def area_of_circle(r):

    if r < 0:
        raise ValueError("Radius cannot be of negative value")

    return pi * r**2
