#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt

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

def graph():
    x = np.linspace(-1, 1, num = 250)
    y = x**2 * np.sin(1/x**2) + x

    # plt.scatter(x,y)
    # plt.xlim(-1,1)
    # plt.title ("Exercise 4")
    # plt.xlabel("x")
    # plt.ylabel ("y")
    # plt.show()

def montecarlo():
    nombredessai = 1000
    xinside = []
    yinside = []
    xoutside = []
    youtside = []
    for i in range (nombredessai):
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 <= 1.0:
            xinside.append(x)
            yinside.append(y)
        else:
            xoutside.append(x)
            youtside.append(y)

    plt.scatter(xinside,yinside)
    plt.scatter(xoutside,youtside)
    plt.title("Calcul de pi par la méthode de Monte Carlo")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return 4*(float(len(xinside)))/nombredessai

    
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print (linear_values())
    print (coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
    print(find_closest_index(np.array([1, 3, 8, 10]), 9.5))
    pass
