"""
Task 9: Спираль
Выведите таблицу (print) размером nxn, заполненную числами от 1 до n^2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке.
"""

import numpy as np

n = 7

def task9(n):
    z = np.zeros((n, n))
    counter = 1
    dop = 0

    for i in range(n):
        
        for j in range(n - i - dop):
            z[i][j + dop] = counter
            counter += 1

        print(str(i) + '.1')
        print(z)
        
        for j in range(i + 1, n - i):
            z[j][n - 1 - i] = counter
            counter += 1
        
        print(str(i) + '.2')
        print(z)

        for j in range(i + 1, n - i):
            if j == n:
                continue
            z[n - 1 - i][n - 1 - j] = counter
            counter += 1
        
        print(str(i) + '.3')
        print(z)

        for j in range(i + 1, n - i - dop):
            if j == n - 1 - dop:
                continue
            z[n - 1 - j][i] = counter
            counter += 1

        print(str(i) + '.4')
        print(z)

        dop += 1

task9(n)