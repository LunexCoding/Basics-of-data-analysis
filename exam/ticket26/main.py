import numpy as np


class DataAnalysis:
    '''
    Создать структурированный массив, представляющий координату (x,y) и цвет (r,g,b).
    '''

    def __init__(self):
        self._array = np.zeros(10, [
            (
                'position', [
                ('x', float, 1),
                ('y', float, 1)
                ]   
            ),
            (
                'color', [
                ('r', float, 1),
                ('g', float, 1),
                ('b', float, 1)
                ]
            )
                ]
            )

    @property
    def array(self):
        return self._array


task = DataAnalysis()
print(task.array)