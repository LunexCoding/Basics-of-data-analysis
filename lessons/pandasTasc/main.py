import pandas as pd
import numpy as np
from numpy import std, mean
import more_itertools

#1
print(pd.Series([1, 2, 5, 8]))

#2
print(pd.Series([1, 2, 5, 8]).tolist())

#3
print(f'Сложение:\n{pd.Series([1, 2, 5, 8]) + pd.Series([1, 2, 5, 8])}',
      f'Умножение:\n{pd.Series([1, 2, 5, 8]) * pd.Series([1, 2, 5, 8])}',
      f'Деление:\n{pd.Series([1, 2, 5, 8]) / pd.Series([1, 2, 5, 8])}', sep='\n')

#4
data1 = pd.Series([2, 4, 6, 8, 10])
data2 = pd.Series([1, 3, 5, 7, 10])
print(f'data1 равно data2:\n{data1 == data2}',
      f'data1 больше data2:\n{data1 > data2}',
      f'data1 меньше data2:\n{data1 < data2}', sep='\n')

#5
print(pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}))

#6
print(pd.Series(np.array([10, 20, 30, 40, 50])))

#7
print(pd.to_numeric(pd.Series([100, 200, 'питона', 300.12, 400]), errors='coerce'))

#8
print(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4], 'col3': [4, 5]}).get('col1'))

#9
print(pd.Series(['100', '200', 'python', '300.12', '400']).tolist())

#13
print([el for el in pd.Series([num for num in range(1, 10)]) if el >= 5])

#15
print(f'Среднее: {mean(pd.Series([num for num in range(1, 10)]))}',
      f'Отклонение: {std(pd.Series([num for num in range(1, 10)]))}', sep='\n')

#10
print(pd.Series(list(more_itertools.flatten([[1, 2, 3], [2, 5], [2]]))))

#11, 12, 14