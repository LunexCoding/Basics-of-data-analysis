class DataAnalysis:
    '''
    Заполнить список квадратами чисел от 0 до 9, используя генератор списка.
    Заполнить список числами, где каждое последующее число больше на 2.
    '''

    def __init__(self):
        pass

    def getArraySquares(self):
        return self._getArraySquares()

    def _getArraySquares(self):
        return [x ** 2 for x in range(10)]

    def getArrayFromRangeWithCondition(self):
        return self._getArrayFromRangeWithCondition()

    def _getArrayFromRangeWithCondition(self):
        return [(x + 1) + x for x in range(10)]


task = DataAnalysis()
print(task.getArraySquares())
print(task.getArrayFromRangeWithCondition())