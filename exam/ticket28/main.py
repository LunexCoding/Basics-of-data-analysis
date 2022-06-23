import numpy as np


class DataAnalysis:
    '''
    Преобразовать массив из float в int.
    '''

    def __init__(self, array=None):
        self._array = array
        print(self._arrayFloatToInt())

    def _arrayFloatToInt(self):
        return self._array.astype(float, copy=False)


task = DataAnalysis(np.random.randint(1, 10, size=[5, 5]))