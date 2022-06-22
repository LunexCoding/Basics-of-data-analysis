class Number:
    '''
    Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.
    '''

    def __init__(self, num=None):
        self._num = num 

    def __add__(self, other):
        return abs(self._num + other._num)


numFirst = Number(3)
numSecond = Number(1)
print(numFirst + numSecond)

