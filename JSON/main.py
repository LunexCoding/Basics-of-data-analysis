import json

#  Сериализация
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

#  объект данных, который сериализуется и, файловый объект, в который будут вписаны байты.
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

#  Склонны продолжать использовать эти сериалзированные данные JSON в вашей программе, можете работать как со строкой.
json_string = json.dumps(data)
print(json_string)

#  Десериализация
#   Результат этого метода может вернуть любые доступные типы данных из таблицы конверсий.
#   Это важно только в том случае, если вы загружаете данные, которые вы ранее не видели.
#   В большинстве случаев, корневым объектом будет dict или list.
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

#  Если вы внесли данные JSON из другой программы, или полученную каким-либо другим способом строку JSON
#  форматированных данных в Python, вы можете легко десериализировать это при помощи loads(), который
#  естественно загружается из строки:
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(json_string)