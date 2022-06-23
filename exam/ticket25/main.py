import numpy as np


class DataAnalysis:
    '''
    Найти минимальное и максимальное значение, принимаемое каждым числовым типом NumPy.
    '''

    def __init__(self):
        self._getData()

    def _getData(self):
        for dtype in [np.int8, np.int32, np.int64]:
            print(np.iinfo(dtype).min)
            print(np.iinfo(dtype).max)
        for dtype in [np.float32, np.float64]:
            print(np.finfo(dtype).min)
            print(np.finfo(dtype).max)
            print(np.finfo(dtype).eps)


task = DataAnalysis()