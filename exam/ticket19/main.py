class DataAnalysis:
    '''
    В массиве целых чисел все отрицательные элементы заменить на положительные.
    Вывести исходный массив и полученный.
    '''

    def __init__(self, array=None):
        self._array = array
        self._newAbsArray = self._absArray(self._array.copy())

    def _absArray(self, array):
        return [abs(x) for x in array]

    def __str__(self):
        return f'Исходный: {self._array}, новый: {self._newAbsArray}'


print(DataAnalysis([3, -3, 2, -6, -2, 1]))

