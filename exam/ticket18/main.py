from random import randint, sample


class DataAnalysis:
    '''
    Из массива X длиной n, среди элементов которого есть положительные, отрицательные и равные нулю,
    сформировать новый массив Y, взяв в него только те элементы из X, которые больше по модулю заданного числа M.
    Вывести на экран число M, данный и полученные массивы.
    '''

    def __init__(self, low=None, high=None):
        self._low = low
        self._high = high

        self._n = 0
        self._M = 0

        while self._n == 0:

            self._n, self._M = self._generateParams()

        self._X = self._generateArray()
        self._Y = [num for num in self._X if abs(num) > abs(self._M)]
       
    def _generateParams(self):
        if self._low > self._high:
            self._low, self._high = self._high, self._low
        return abs(randint(self._low, self._high)), randint(self._low, self._high)

    def _generateArray(self):
        return sample(range(self._low, self._high), self._n)

    def data(self):
        return f'M: {self._M}', f'n: {self._n}', f'X: {self._X}', f'Y: {self._Y}'


task = DataAnalysis(-10, 10)
for el in task.data():
    print(el)

