import numpy as np


class DataAnalysis:
    '''
    Поменять 2 строки в матрице.
    '''

    def __init__(self, matrix=None, indexs=None):
        self._matrix = matrix
        self.showMatrix()
        self._firstIndex, self._secondIndex = indexs
        self._swapMatrixRows()
        self.showMatrix()

    def _swapMatrixRows(self):
        self._matrix[[self._firstIndex, self._secondIndex]] = self._matrix[[self._secondIndex, self._firstIndex]]

    def showMatrix(self):
        print(self._matrix)


task = DataAnalysis(np.random.randint(1, 10, size=[5, 5]), [2, 3])
