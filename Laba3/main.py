from consoleAPI.colorCommands.DeleteColorCommand import DeleteColorCommand
from consoleAPI.colorCommands.UpdateColorCommand import UpdateColorCommand
from consoleAPI.colorCommands.GetColorByIdCommand import GetColorByIdCommand
from consoleAPI.colorCommands.AddColorCommand import AddColorCommand
from feature.countProductsForEachColor import countProductsForEachColor
from entity.Product import Product
from entity.TypeProduct import TypeProduct
from entity.Color import Color
from data.SQLiteConnector import SQLiteConnector
from data.repository.ColorRepository import ColorRepository
from data.repository.ProductRepository import ProductRepository
from data.repository.TypeProductRepository import TypeProductRepository
import csv


if __name__ == '__main__':
    DB_PATH = './Laba3/db/laba3_db.db'
    SCRIPT_PATH = './Laba3/db/create_schema.sql'

    connector = SQLiteConnector(DB_PATH)
    colorRepo = ColorRepository(connector)
    typeProductRepo = TypeProductRepository(connector)
    productRepo = ProductRepository(connector)
    
    # # добавление цветов
    # colorRepo.add(Color('black'))
    # colorRepo.add(Color('white'))
    # colorRepo.add(Color('green'))

    # # добавление типов товаров
    # typeProductRepo.add(TypeProduct('Электроника'))
    # typeProductRepo.add(TypeProduct('Телефоны'))
    # typeProductRepo.add(TypeProduct('Аксессуары'))

    # # получение цветов из бд
    # black = colorRepo.getById(1)
    # white = colorRepo.getById(2)
    # green = colorRepo.getById(3)

    # # получение типов товаров из бд
    # electronices = typeProductRepo.getById(1)
    # phones = typeProductRepo.getById(2)
    # accessories = typeProductRepo.getById(3)

    # # добавление товаров
    # productRepo.add(Product('Беспроводные наушники A6RDots TWS', 575, electronices, 1, green))
    # productRepo.add(Product('Батарейки 2032, 3В, 2шт', 205, electronices, 1, black))
    # productRepo.add(Product('Samsung S7', 25999.67, phones, 1, black))
    # productRepo.add(Product('IPhone 14 Pro MAX', 149990.57, phones, 1, white))
    # productRepo.add(Product('Кабельный органайзер', 359, accessories, 1, black))
    # productRepo.add(Product('Чехол для хранения наручных часов', 550, accessories, 1, green))

    # # получение товара из бд по id
    # product = productRepo.getById(1)
    # print(product)

    # # Работа с CSV
    # with open('./Laba3/datas.csv', mode='w', encoding='utf-8') as wFile:
    #     file_writer = csv.writer(wFile, delimiter = ',', lineterminator='\r')
    #     file_writer.writerow(['id', 'Название', 'Цена', 'ID_Вида_Товара', 'Наличие в магазине', 'ID_Цвета'])
    #     file_writer.writerow([product.id, product.productName, product.price, product.typeProduct.id, product.availability, product.color.id])

    # with open('./Laba3/datas.csv', encoding='utf-8') as rFile:
    #     file_reader = csv.reader(rFile, delimiter = ",")
    #     count = 0
    #     for row in file_reader:
    #         if count == 0:
    #             print(f'Файл содержит столбцы: {", ".join(row)}')
    #         else:
    #             # print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
    #             product_id, product_name, product_price, type_id, product_availability, color_id = row
    #             print(product_id, product_name, product_price, type_id, product_availability, color_id)
    #         count += 1
    #     print(f'Всего в файле {count} строк.')

    commands = [
        GetColorByIdCommand(colorRepo),
        AddColorCommand(colorRepo),
        DeleteColorCommand(colorRepo),
        UpdateColorCommand(colorRepo),
    ]

    line = input()
    parts = line.split(' ')
    nameCommand = parts[0]
    
    command = list(filter(lambda x: x.name == nameCommand, commands))
    if len(command) != 0:
        command[0].handle(parts[1:])



'''
color's commands
-----------------------------------------
get_color_by_id [id]
add_color [name]
delete_color [id]
update_color [prev_id] [new_name]

type produpct's commands
-----------------------------------------
get_type_product_by_id [id]
add_type_product [name]
delete_type_product [id]
update_type_product [prev_id] [new_name]

product's commands
-----------------------------------------
get_product_by_id [id]
add_product [name] [price] [type_id] [availability] [color_id]
delete_type_product [id]
update_type_product [prev_id] [new_name] [new_price] [new_type_id] [new_availability] [new_color_id]

general commands
count_products_for_each_color
'''