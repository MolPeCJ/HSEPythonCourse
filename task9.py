"""
Task 9: Спираль
Выведите таблицу (print) размером nxn, заполненную числами от 1 до n^2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке.
"""

n1 = 4
n2 = 6

def task9(n: int) -> None:
    z = [[0]*n for _ in range(n)]
    counter = 1
    dop = 0

    for i in range(n):
        
        for j in range(n - i - dop):
            z[i][j + dop] = counter
            counter += 1
        
        for j in range(i + 1, n - i):
            z[j][n - 1 - i] = counter
            counter += 1
        
        for j in range(i + 1, n - i):
            if j == n:
                continue
            z[n - 1 - i][n - 1 - j] = counter
            counter += 1

        for j in range(i + 1, n - i - dop):
            if j == n - 1 - dop:
                continue
            z[n - 1 - j][i] = counter
            counter += 1
        
        dop += 1

    for row in z:
        print(*row)

# Проверки

task9(n1)
print('-----')
task9(n2)
