"""
Task8: Дополнить класс расчетом метрик
Вам дан класс, необходимо дописать расчет различных метрик. 
Подробнее см. task8.py. P.S. при расчете статистик можете принебречь степенями свободы.
"""

from typing import Union, List, Tuple
import numpy as np
import scipy.stats as ss

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
        return ss.mode(self).mode
    
    def std(self) -> float | int:
        # считаем стандартное отклонение (не дисперсию)
        return np.std(self)
    
    def iqr(self) -> float | int:
        # считаем интерквартильный размах: https://shorturl.at/rsuBK
        return np.percentile(self, 75) - np.percentile(self, 25)