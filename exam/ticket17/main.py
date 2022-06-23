class DataAnalysis:
    '''
    Определить длину строки.
    ЕСЛИ длина строки превышает 4 символа, ТО вывести строку в нижнем регистре.
    Заменить в строке первый символ на 'О'. Результат вывести на экран.
    '''

    def __init__(self, string=None, firstLetter=None):
        self._string = string
        self._firstLetter = firstLetter
        self._replaceFirstLetter()

    def _replaceFirstLetter(self):
        self._string = self._string[:0] + self._firstLetter + self._string[0 + 1:]

    @property
    def string(self):
        return self._string.lower() if self.len > 4 else self._string

    @property
    def len(self):
        return len(self._string)


task = DataAnalysis("У лукоморья 123 дуб зеленый 456", 'О')
print(task.string)