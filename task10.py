"""
Task10: Евклидово расстояние
На вход подается np.ndarray размерности N x M, где (2 <= N, M <= 10^3). 
Каждая строка - вектор, необходимо составить матрицу размера NxN, где [i,j] элемент будет соответствовать евклидову расстоянию между векторами i и j.
"""

import numpy as np
import scipy.spatial as ss

example = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [-2, 5, 4]])

def task10(matrix: np.ndarray) -> np.ndarray:
    z = np.eye((len(matrix)))

    for i in range(len(z)):
        for j in range(len(z)):
            z[i][j] = ss.distance.euclidean(matrix[i], matrix[j])

    print(z)

# Альтернативное решение

def task10_1(matrix: np.ndarray) -> np.ndarray:
    dist_matrix = ss.distance_matrix(matrix, matrix)

    print(dist_matrix)

# Проверки

task10(example)
print('-----')
task10_1(example)