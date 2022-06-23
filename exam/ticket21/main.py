from random import randrange


class DataAnalysis:
    '''
    В массиве действительных чисел все нулевые элементы заменить на среднеарифметическое всех элементов массива.
    '''

    def __init__(self, low=None, high=None, count=None):
        self._low = low
        self._high = high
        self._count = count
        self._array = self._generateArray()
        self._mean = self._getMean()
        self._replaceZero()

    def _generateArray(self):
        return [randrange(self._low, self._high) for i in range(self._count)]

    def _getMean(self):
        return sum(self._array) / len(self._array)

    def _replaceZero(self):
        self._array = [self._mean if x == 0 else x for x in self._array]

    @property
    def array(self):
        return self._array


task = DataAnalysis(0, 2, 5)
print(task.array)