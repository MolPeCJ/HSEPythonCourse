"""
Task7: Максимальный палиндром
На вход подается строка, содержащая буквы алфавита в нижнем регистре. 
Найдите максимальный палиндром, который можно составить из этих букв и выведите его длину.
"""

from collections import Counter

row1 = 'aab'    # 3
row2 = 'abcdba' # 5
    
def task7(row):
    chars_count = Counter(row)
    length = 0
    has_odd = False

    for count in chars_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True

    if has_odd:
        length += 1

    return length

print(task7(row1))
print(task7(row2))

print(task7(input('Введите строку для анализа: ')))
