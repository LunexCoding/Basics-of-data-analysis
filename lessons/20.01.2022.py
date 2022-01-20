import pandas as pd
with open('files/20.01.2022/Fairy-tale heroes.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    del data[0]
    del data[0]

    data = [el.split() for el in data]
    names = []
    col1 = []
    col2 = []

    for i in range(len(data)):
        if len(data[i]) == 3:
            names.append(data[i][0])
            col1.append(data[i][1])
            col2.append(data[i][2])
        else:
            names.append(data[i][0] + ' ' + data[i][1])
            col1.append(data[i][2])
            col2.append(data[i][3])


    table = pd.concat([pd.Series(names).to_frame(name='name'), pd.Series(col1).to_frame(name='оценка'),
                       pd.Series(col2).to_frame(name='баллы')], axis=1)

    table.index = [num for num in range(1, 21)]
    print(table)