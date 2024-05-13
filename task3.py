"""
Task3: Возрастает ли список?
Дан список. Определите, является ли он монотонно возрастающим (то есть верно ли, что каждый элемент этого списка больше предыдущего).
"""

from typing import List

values_1 = [-1, 1, 2, 5, 9, 10, 114, 230]       # True
values_2 = [-5, -8, -124, -93, -41, -72]        # False
values_3 = [1, -5, -121, 115, 19, -5, -23, 27]  # False
values_4 = [1, 2, 3, 4]                         # True
values_5 = [2, 2, 2]                            # False

def task3(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            continue
        else:
            return 'False'
        
    return 'True'

# Проверки
 
print(task3(values_1))
print(task3(values_2))
print(task3(values_3))
print(task3(values_4))
print(task3(values_5))
