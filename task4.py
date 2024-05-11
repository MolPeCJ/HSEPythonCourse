"""
Task4: Количество уникальных гласных
На вход подается строка, выведите количество уникальных гласных в ней (гласные это [а,у,о,ы,э,я,ю,ё,и,е]).
"""

row1 = 'ауеив' # 4
row2 = 'ааааа' # 1

vowels = list(set('ауoыэяюёие'))

def task4(row):
    letters = list(set(row))
    count = 0

    for letter in letters:
        if letter in vowels:
            count += 1
    
    return count

print(task4(row1))
print(task4(row2))

print(task4(input('Введите строку для анализа: ')))
