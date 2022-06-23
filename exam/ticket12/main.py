class DataAnalysis:
    '''
    Дано вещественное число – цена 1 кг конфет.
    Вывести стоимость 1, 2, … 10 кг конфет.
    Решить задачу используя циклическую конструкцию for.
    '''

    def __init__(self, cost=None):
        self._cost = cost
        self._costPerKilogram = {}
        self._calcCosts()

    def _calcCosts(self):
        for i in range(1, 11):
            self._costPerKilogram[i] = i * self._cost

    def showCost(self):
        for key, value in self._costPerKilogram.items():
            print(f'Стоимость за {key} кг - {value}')


task = DataAnalysis(10)
task.showCost()
