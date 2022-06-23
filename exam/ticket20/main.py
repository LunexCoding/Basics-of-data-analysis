class DataAnalysis:
    '''
    Дан одномерный массив, состоящий из N целочисленных элементов.
    Ввести массив с клавиатуры.
    Найти максимальный элемент.
    Вывести массив на экран в обратном порядке.
    '''

    def __init__(self, array=None):
        self._array = array
        print(f'Max: {self._getMax()}')
        print(f'Reverse array: {self._getReverseArray()}')

    def _getMax(self):
        return max(self._array)

    def _getReverseArray(self):
        return self._array[::-1]


DataAnalysis(list(map(int, input('-> ').split())))    