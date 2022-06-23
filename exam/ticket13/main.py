class DataAnalysis:
    '''
    Дана непустая последовательность целых чисел, оканчивающаяся нулем.
    Найти:
        а) сумму всех чисел последовательности;
        б) количество всех чисел последовательности.
    Решить задачу используя циклическую конструкцию while.
    '''

    def __init__(self):
        self._array = []
        self._inputArray()

    def _inputArray(self):
        number = None
        while number != 0:
            number = int(input('-> '))
            self._array.append(number)

    @property
    def sum(self):
        return sum(self._array)

    @property
    def len(self):
        return len(self._array)


array = DataAnalysis()
print(f'Сумма: {array.sum}, длина {array.len}')
