<h1 align='center'>Билет 1</h1>

1. Что такое Seaborn. Для чего используется Seaborn.

    **Seaborn** - это библиотека визуализации данных Python, предоставляющая высокоуровневый интерфейс для рисования привлекательных и информативных статистических графиков.

2. Какой командой в Seaborn можно установить тему графика?

    ```python
    import seaborn as sns
    sns.set_theme()
    ```

# Практика

```python
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
        plt.savefig('ticket1.png')
        plt.show(block=True)

    @property
    def data(self):
        return self._data

task = DataAnalysis('../assets/tips.csv')
task.buildGraph()
```
