"""
Task8: Дополнить класс расчетом метрик
Вам дан класс, необходимо дописать расчет различных метрик. 
Подробнее см. task8.py. P.S. при расчете статистик можете принебречь степенями свободы.
"""

from typing import Union, List, Tuple
import numpy as np

values = [1, 1, 51, 1234, 401, -2100, -2100, 123, 4, 4, 1234, -2100]

class Statistics:
    def __init__(self, data: Union[List[int|float], Tuple[int|float], np.ndarray[int|float]]):
        """
        Пара моментов:
            1. массив всегда 1D, т.е. просто вектор
            2. степенями свободы можете принебречь
        """
        self.data = data
        
    def calculate_mean(self) -> float | int:
        # считаем среднюю от self.data
        return np.mean(self)
        
    def calculate_median(self) -> float | int:
        # считаем медиану от self.data
        return np.median(self)
        
    def calculate_mode(self) -> float | int:
        # считаем моду от self.data
        """
        в случае если два и более объекта встречаются одинаковое количество раз
        модой будет наибольший из них
        
        Пример1:
        data = [1,2,2,3]
        out: 2
        
        Пример2:
        data = [1,2,3]
        out: 3
        """
        mode, count = np.unique(self, return_counts = True)
        max_value = float('-inf')

        for i in range (len(mode)):
            if count[i] == max(count) and mode[i] > max_value:
                max_value = mode[i]
        
        return max_value
    
    def std(self) -> float | int:
        # считаем стандартное отклонение (не дисперсию)
        return np.std(self)
    
    def iqr(self) -> float | int:
        # считаем интерквартильный размах: https://shorturl.at/rsuBK
        return np.percentile(self, 75) - np.percentile(self, 25)
    
# Проверки

print('Cредняя:', Statistics.calculate_mean(values))
print('Медиана:', Statistics.calculate_median(values))
print('Мода:', Statistics.calculate_mode(values))
print('Стандартное отклонение:', Statistics.std(values))
print('Интерквартильный размах:', Statistics.iqr(values))
