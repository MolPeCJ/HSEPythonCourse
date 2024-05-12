"""
Task10: Евклидово расстояние
На вход подается np.ndarray размерности N x M, где (2 <= N, M <= 10^3). 
Каждая строка - вектор, необходимо составить матрицу размера NxN, где [i,j] элемент будет соответствовать евклидову расстоянию между векторами i и j.
"""

import numpy as np
import scipy.spatial as ss

example = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [-2, 5, 4]])

z = np.eye((len(example)))

for i in range(len(z)):
    for j in range(len(z)):
        z[i][j] = ss.distance.euclidean(example[i], example[j])

print(z)

# Алтернативное решение

dist_matrix = ss.distance_matrix(example, example)

print(dist_matrix)