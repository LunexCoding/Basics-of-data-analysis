class DataAnalysis:
    '''
    В строке удалить символ точку (.) и подсчитать количество удаленных символов.
    В строке заменить букву (а) буквой (о).
    Подсчитать количество замен.
    Подсчитать сколько символов в строке.
    '''

    def __init__(self, string=None):
        self._string = string
        self._countDeletedLetter = 0
        self._countReplace = 0

    def deleteLetter(self, letter):
        self._deleteLetter(letter)
        return self.countDeletedLetter

    def _deleteLetter(self, letter):
        lenBeforeDelete = self.len
        self._string = self._string.replace(letter, '')
        self._countDeletedLetter = lenBeforeDelete - self.len

    @property
    def countDeletedLetter(self):
        return self._countDeletedLetter 

    def replace(self, oldLetter, newLetter):
        self._replace(oldLetter, newLetter)
        return self.string

    def _replace(self, oldLetter, newLetter):
        self._string = self._string.replace(oldLetter, newLetter)
    
    @property
    def string(self):
        return self._string

    @property
    def len(self):
        return len(self._string)

letter, oldLetter, newLetter = '.', 'а', 'о'
task = DataAnalysis('Кластерный анализ – группа методов, используемых для классификации\
 объектов или событий в относительно гомогенные (однородные) группы, которые называют кластерами (clusters).')
print(
    f'Кол-во удалений "{letter}": task.deleteLetter(letter)',
    f'Строка: {task.replace(oldLetter, newLetter)}',
    f'Длина строки: {task.len}',
    sep='\n'
)
