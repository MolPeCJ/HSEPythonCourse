"""
Task5: Палиндром
На вход подается строка, выведите True если она является палиндромом и False иначе.
"""

row1 = 'acbca' # True
row2 = 'ab'    # False

def task5(row):
    return True if row == row[::-1] else False

print(task5(row1))
print(task5(row2))

print(task5(input('Введите строку для анализа: ')))
