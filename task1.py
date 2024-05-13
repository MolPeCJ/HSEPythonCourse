"""
Task1: Наибольшее произведение двух чисел
Дан список, заполненный произвольными целыми числами. 
Найдите в этом списке два числа, произведение которых максимально. 
Выведите эти числа в любом порядке. Если таких комбинаций больше 1, выведите любую.
"""

from typing import List

values_positive = [1, 5, 2, 9, 0, 11, 14, 23]    # [23, 14]
values_negative = [-5, -8, -124, -93, -41, -3]   # [-124, -93]
values_any = [1, -5, -121, 115, 19, -5, -23, 27] # [115, 27]

def task1(l: List[int]) -> List[int]:
    max1, max2 = -1e6, -1e6
    min1, min2 = 1e6, 1e6

    for value in l:
        if value >= max1:
            max2 = max1
            max1 = value
        elif value > max2:
            max2 = value

        if value <= min1:
            min2 = min1
            min1 = value
        elif value < min2:
            min2 = value
    
    if max1 * max2 >= min1 * min2:
        return [max1, max2]
    else:
        return [min1, min2]
    
# Проверки
    
print(task1(values_positive))
print(task1(values_negative))
print(task1(values_any))
