"""
Task6: Наибольшая подстрока палиндром
На вход подается строка, найдите максимальную по длине подстроку, которая является палиндромом и выведите ее длину.
"""

row1 = 'cdaaabca' # 3
row2 = 'ab'       # 1
row3 = 'aaaaaab'  # 6

def task6(row):
    letters = list(row)
    rows = []
    
    if len(letters) == 1:
        return 1

    for i in range(len(letters) - 1):
        row_for_analysis = letters[i]

        for j in range(i + 1, len(letters)):
            row_for_analysis += letters[j]

            if row_for_analysis == row_for_analysis[::-1]:
                rows.append(len(row_for_analysis))
    
    if len(rows) >= 1:
        return max(rows)
    else:
        return 1

print(task6(row1))
print(task6(row2))
print(task6(row3))

print(task6(input('Введите строку для анализа: ')))
