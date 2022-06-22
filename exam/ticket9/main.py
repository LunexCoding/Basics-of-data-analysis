class DataAnalysis:
    '''
    Даны три целых числа. Выбрать из них те, которые принадлежат интервалу [1, 3].
    '''

    def __init__(self, lowerLimit=None, upperLimit=None, *nums):
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        self._num1, self._num2, self._num3 = nums
        self._numsInBetween = []

    def getNumsInBetween(self):
        for num in [self._num1, self._num2, self._num3]:
            if num >= 1 and num <= 3:
                self._numsInBetween.append(num)
        return self._numsInBetween


task = DataAnalysis(1, 3, 1, 4, 6)
print(task.getNumsInBetween())