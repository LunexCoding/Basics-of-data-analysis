class DataAnalysis:
    '''
    Составить программу, которая изменяет последовательность слов в строке на обратную.
    '''

    def __init__(self, string=None):
        self._string = string
        print(self._getString())

    def _getString(self):
        return ' '.join(self._string.split(" ")[::-1])


task = DataAnalysis('Составить программу, которая изменяет последовательность слов в строке на обратную.')