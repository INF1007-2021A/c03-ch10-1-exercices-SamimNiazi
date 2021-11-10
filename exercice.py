#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import cmath
import math

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values(min: float = -1.3, max: float = 2.5, nb_delem: float = 64) -> np.ndarray:
    return np.linspace(min, max, nb_delem)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:   
    return np.array([((math.sqrt(x_and_y[0]**2 + x_and_y[1]**2)), math.atan2(x_and_y[1], x_and_y[0])) for x_and_y in cartesian_coordinates])
    


def find_closest_index(values: np.ndarray, number: float) -> int:
    current = values[0]
    
    for element in values:
        if abs(element - number) < abs(current - number):
            current = element
    index, = np.where(values == current)
    return index


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print (linear_values())
    print (coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
    print(find_closest_index(np.array([1, 3, 8, 10]), 9.5))
    pass
