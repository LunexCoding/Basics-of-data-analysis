import seaborn as sns 
import matplotlib.pyplot as plt

sns.set_theme()


class DataAnalysis:
    '''
    Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.
    '''

    def __init__(self, filename):
        self._filename = filename
        self._data = sns.load_dataset('tips')

    def buildGraph(self):
        graph = sns.relplot(
            data=self._data,
            x='total_bill',
            y='tip',
            col='time',
            hue='sex',
            style='smoker',
            size='size'
        )
        plt.savefig(self._filename)
        plt.show(block=True)

    @property
    def data(self):
        return self._data

task = DataAnalysis('ticket1.png')
task.buildGraph()