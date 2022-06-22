<h1 align='center'>Билет 4</h1>

1.	Списки в Python — это. С помощью чего можно создать список?

    * []
    * list()
    * [x for x in string]

2. Функция list(). Для чего используется?

    Создать список

# Практика

```python
class DataAnalysis:
    '''
    Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
    В исходном списке минимум 2 элемента.
    '''

    def __init__(self, array=None):
        self._array = array

    def change(self):
        self._array[0], self._array[1] = self._array[1], self._array[0]


list_ = [1, 4, 5, 2, 7]    
task = DataAnalysis(list_)
task.change()
print(list_)
```