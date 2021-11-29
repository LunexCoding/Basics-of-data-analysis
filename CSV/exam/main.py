import csv
from statistics import mode
from numpy import median, std


def getStdev(parameter, data):
    return f'Parameter: {parameter}, Результат: {std(data)}'

def getMode(parameter, data):
    return f'Parameter: {parameter}, Результат: {mode(data)}'

def getMean(parameter, data): #среднее
    return f'Parameter: {parameter}, Результат: {sum(data) / len(bigData)}'

def getMedian(parameter, data):
    return f'Parameter: {parameter}, Результат: {median(data)}'

def getSum(parameter, data):
    return f'Parameter: {parameter}, Результат: {sum(data)}'

def getMaxMin(parameter, data):
    return f'Parameter: {parameter}, Результат:\n   Max: {max(data)}\n   Min: {min(data)}'


with open('diamonds.csv') as file:
    reader = csv.reader(file, delimiter=',')

    bigData = (list(reader))

    del bigData[0]

    parameters = {'carat': [float(row[1]) for row in bigData],
                  'price': [float(row[7]) for row in bigData],
                  'x': [float(row[-3]) for row in bigData],
                  'y': [float(row[-2]) for row in bigData],
                  'z': [float(row[-1]) for row in bigData]}

for key in parameters:
    print(getStdev(key, parameters[key]))
    print(getMode(key, parameters[key]))
    print(getMean(key, parameters[key]))
    print(getMedian(key, parameters[key]))
    print(getSum(key, parameters[key]))
    print(getMaxMin(key, parameters[key]))

