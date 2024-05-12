"""
Task2: Наибольшее произведение трех чисел
Дан список, заполненный произвольными целыми числами. 
Найдите в этом списке ТРИ числа, произведение которых максимально. 
Выведите эти числа в любом порядке. Если таких комбинаций больше 1, выведите любую.
"""

values_positive = [1, 2, 3, 4]                   # [4, 3, 2]
values_negative = [-1, -2, -3, 4]                # [4, -3, -2]
values_any = [1, -5, -121, 115, 19, -5, -23, 27] # [115, -121, -23]
 
def task2(values):
    values.sort(reverse = True)
    max_positive = values[0] * values[1] * values[2]
    max_mix = values[0] * values[-1] * values[-2]

    if max_positive > max_mix:
        return [values[0], values[1], values[2]]
    else:
        return [values[0], values[-1], values[-2]]

print(task2(values_positive))
print(task2(values_negative))
print(task2(values_any))
