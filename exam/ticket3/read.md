<h1 align='center'>Билет 3</h1>

1. Строки в языке Python (полное определение)

    **Строка** – это последовательность символов, заключенных в одинарные или двойные кавычки.

2. Строки байтов – bytes и bytearray.

    **Байт** - минимальная единица хранения и обработки цифровой информации. Последовательность байт представляет собой какую-либо информацию.

    ```python
    >>> b'bytes'
    b'bytes'
    >>> 'Байты'.encode('utf-8')
    b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'
    >>> bytes('bytes', encoding = 'utf-8')
    b'bytes'
    >>> bytes([50, 100, 76, 72, 41])
    b'2dLH)'
    ```

# Практика

```python
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
```