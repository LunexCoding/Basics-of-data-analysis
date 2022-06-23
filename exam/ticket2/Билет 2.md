<h1 align='center'>Билет 2</h1>

1. Сколько (встроенных) типов чисел есть в языке Python. Напишите их на латинице.

    * INT
    * FLOAT
    * COMPLEX

2. Если частное двух целых чисел (int) не является целым числом, то оно будет преобразовано…

    * float

# Практика

```python
class Number:
    '''
    Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.
    '''

    def __init__(self, num=None):
        self._num = num 

    def __add__(self, other):
        return abs(self._num + other._num)


print(Number(3) + Number(1))
```