"""
Task2: Наибольшее произведение трех чисел
Дан список, заполненный произвольными целыми числами. 
Найдите в этом списке ТРИ числа, произведение которых максимально. 
Выведите эти числа в любом порядке. Если таких комбинаций больше 1, выведите любую.
"""

values_positive = [1, 5, 2, 9, 0, 11, 14, 23]
values_negative = [-5, -8, -124, -93, -41, -3]
values_any = [1, -5, -121, 115, 19, -5, -23, 27]

def task2(values):
    max1, max2 = -1e6, -1e6
    min1, min2 = 1e6, 1e6

    for value in values:
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

    values.sort()
    
    if max1 * max2 >= min1 * min2:
        return [max1, max2, values[-3]]
    else:
        return [min1, min2, values[-1]]

    # if max1 * max2 >= min1 * min2:
    #     return [max1, max2]
    # else:
    #     return [min1, min2]
    
print(task2(values_positive))
print(task2(values_negative))
print(task2(values_any))

# values_any.sort()

# print(values_any)
# print(values_any[3])
# print(values_any[-3])