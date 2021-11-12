import csv
import os

with open('cars.csv', 'r') as file:
    fileReader = csv.reader(file, delimiter=' ')

    if not os.path.isdir("files"):
        os.mkdir("files")
    os.chdir("files")

    with open('newCSVFile.csv', 'w') as file:
        fileWriter = csv.writer(file, delimiter=' ', lineterminator="\r")

        for line in fileReader:
            fileWriter.writerow(line)

        fileWriter.writerow(['add,', 'commit,', 'push'])

with open('newCSVFile.csv', 'r') as file:
    fileReader = csv.reader(file, delimiter=' ')
    for line in fileReader:
        print(' '.join(line))