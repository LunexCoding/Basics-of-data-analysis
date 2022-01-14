def getShortAlphabet():
    number = int(input())
    symbols = list(map(chr, range(65, 90)))
    print(*symbols[::number])
getShortAlphabet()


with open('txt.txt', 'r') as file:
    with open('new.txt', 'r') as new:
        for row in file:
            new.write(' '.join(row.split()).replace(',', ''))


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

