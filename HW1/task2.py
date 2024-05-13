"""
Task2: Наибольшее произведение трех чисел
Дан список, заполненный произвольными целыми числами. 
Найдите в этом списке ТРИ числа, произведение которых максимально. 
Выведите эти числа в любом порядке. Если таких комбинаций больше 1, выведите любую.
"""

from typing import List

values_positive = [1, 2, 3, 4]                   # [4, 3, 2]
values_negative = [-1, -2, -3, 4]                # [4, -3, -2]
values_any = [1, -5, -121, 115, 19, -5, -23, 27] # [115, -121, -23]
 
def task2(l: List[int]) -> List[int]:
    l.sort(reverse = True)
    max_positive = l[0] * l[1] * l[2]
    max_mix = l[0] * l[-1] * l[-2]

    if max_positive > max_mix:
        return [l[0], l[1], l[2]]
    else:
        return [l[0], l[-1], l[-2]]
    
# Проверки

print(task2(values_positive))
print(task2(values_negative))
print(task2(values_any))
