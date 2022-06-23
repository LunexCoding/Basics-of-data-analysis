class DataAnalysis:
    '''
    Создать процедуру для вывода сообщения об ошибке.
    Запрашивать у пользователя ввести положительное число, в случае ввода отрицательного числа,
    вызывать процедуру для вывода сообщения об ошибке.
    '''

    def __init__(self):
        self._input()

    def _input(self):
        assert int(input('-> ')) >= 0, "Negative number"


task = DataAnalysis()