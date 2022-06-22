class DataAnalysis:
    '''
    На входе функция to_set() получает строку или список чисел.
    Преобразуйте их в множество.
    На выходе должно получиться множество и его мощность.
    '''

    def __init__(self, arg):
        self._arg = arg

    def to_set(self):
        return f'{set(self._arg)}, мощность: {len(set(self._arg))}'


task = DataAnalysis([4, 5, 5, 6, 'dgb'])
print(task.to_set())