class DataAnalysis:
    '''
    Дано 3 числа. Найти минимальное среди них и вывести на экран.
    '''

    def __init__(self, *args):
        self._num1, self._num2, self._num3 = args

    def getMinNum(self):
        return min([self._num1, self._num2, self._num3])


task = DataAnalysis(1, 2, 3)
print(task.getMinNum())