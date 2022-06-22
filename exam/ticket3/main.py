class DataAnalysis:
    '''
    Определить, встречается ли в строке буква 'я'.
    Вывести на экран ее позицию (индекс) в строке.
    Определить, сколько раз в строке встречается буква 'у'.
    Определить длину строки.
    '''

    def __init__(self, string=None):
        self._string = string

    def findLetter(self, letter):
        return self._string.index(letter) if True else letter in self._string

    def countLetter(self, letter):
        return f'Длина строки: {len(self._string)}, буква: {letter} встретилась -> {self._string.find(letter)}'


task = DataAnalysis('У лукоморья 123 дуб зеленый 456')
print(task.findLetter('я'))
print(task.countLetter('у'))


    
