# №1 Короткий алфавит

Вывести укороченную версию алфавита в зависимости от введенного числа.

```python
def getShortAlphabet():
    number = int(input())
    symbols = list(map(chr, range(65, 90)))
    print(*symbols[::number])
getShortAlphabet()
```

# №2 Числовой файл

Вывести все числа из файла, убрав лишние пробелы и запятые, оставить табуляцию

```python
with open('txt.txt', 'r') as file:
    for row in file:
        print(' '.join(row.split()).replace(',', ''))
```

# №3 МЕГА-ДАТА

Прочитать файла, вытащить данные в пдф по нужному году.

```python
import csv
with open('globalterrorism.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')

    bigData = list(reader)
    del bigData[0]

    years = []

    for row in bigData:
        if row[1] == '1982' or row[1] == '1983':
            years.append(row)

    with open('data.txt', 'w', encoding='utf-8') as file:
        for rows in years:
            file.write(' '.join(rows) + '/n')
 ```