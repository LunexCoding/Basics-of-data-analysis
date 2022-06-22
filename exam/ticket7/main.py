import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


class DataAnalysis:
    '''
    Постройте простой график на основе встроенного набора данных flights,
    который содержит информацию о месячном объеме пассажироперевозок в период с 1945 по 1960 год.
    Строки – сколько пассажиров было перевезено в определенном месяце определенного года,
    столбцы – год, месяц и количество.
    '''

    def __init__(self, filename):
        self._filename = filename
        self._flights = sns.load_dataset("flights")

    def buildGraph(self):
        sns.relplot(
            data=self._flights,
            x='year',
            y='passengers',
            kind='line'
            )
        plt.savefig(self._filename)
        plt.show(block=True)

    @property
    def data(self):
        return self._data

task = DataAnalysis('ticket7.png')
task.buildGraph()

