import numpy as np


class DataAnalysis:
    '''
    Дан двумерный массив. Найти все различные строки.
    '''

    def __init__(self, matrix=None):
        self._matrix = matrix
        print(self._findDifferentStrings())

    def _findDifferentStrings(self):
        temp = np.ascontiguousarray(self._matrix).view(np.dtype((np.void, self._matrix.dtype.itemsize * self._matrix.shape[1])))
        _, idx = np.unique(temp, return_index=True)
        return self._matrix[idx]


task = DataAnalysis(np.random.randint(0, 2, (6, 3)))