class DataAnalysis:
    '''
    Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
    в котором каждый элемент списка является и ключом, и значением.
    Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
    '''

    def __init__(self, list_=None):
        self._list = list_
        print(self._list)

    def to_dict(self):
        return {key: value for key, value in zip(self._list, self._list)}
        

task = DataAnalysis([1, 3, 'fgd', 'dfg', (3, 4)])
print(task.to_dict())
