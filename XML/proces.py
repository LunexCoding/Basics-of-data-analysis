import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def create():
    """Создаем структуру подобную HTML"""
    #  Родительский (главный) блок HTML, в нашем случае data (название можно задать любое)
    data = ET.Element("data")

    #  Дочерний блок-обертка, находящийся в блоке data
    items = ET.SubElement(data, "items")

    #  Элементы - дочерние блоки, блока-обертки items
    ET.SubElement(items, "item", name="item1").text = "text-item1"
    ET.SubElement(items, "item", name="item2").text = "text-item2"

    #  Создание структуры - дерева
    tree = ET.ElementTree(data)

    if not os.path.isdir("files"):
        os.mkdir("files")
    os.chdir("files")

    #  Запись структуры в файл
    tree.write("XML.xml")


def processing():
    """Реализация интерфейса объектной модели документа с API"""
    xml = minidom.parse('XML.xml')

    #  Вытащим блоки по их названию
    items = xml.getElementsByTagName('item')

    #  атрибуты всех элементов
    print('\nAll attributes:')
    for elem in items:
        print(elem.attributes['name'].value)

    #  данные всех элементов
    print('\nAll item data:')
    for elem in items:
        print(elem.firstChild.data)
    print()

def edit():
    """Изменение XML"""
    #  Импорт данных из файла
    tree = ET.parse('XML.xml')

    #  Предоставление прав для редактирования файла
    root = tree.getroot()

    #  Изменение данных для блоков-элементов item
    for elem in root.iter('item'):
        elem.text = input(f'Input new text for {elem.attrib["name"]} element -> ')

    #  Запись в файл
    tree.write('newXML.xml')

create()
processing()
edit()