import numpy as np


class DataAnalysis:
    '''
    Случайно расположить p элементов в 2D массив.
    '''

    def __init__(self, p=None):
        self._p = p
        print(self._getMatrix())

    def _getMatrix(self):
        return np.random.randint(1, 10, size=[self._p, self._p])


task = DataAnalysis(5)
