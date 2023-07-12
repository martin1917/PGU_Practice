from consoleAPI.Command import BaseCommand
from consoleAPI.colorCommands.DeleteColorCommand import DeleteColorCommand
from consoleAPI.colorCommands.UpdateColorCommand import UpdateColorCommand
from consoleAPI.colorCommands.GetColorByIdCommand import GetColorByIdCommand
from consoleAPI.colorCommands.AddColorCommand import AddColorCommand

from consoleAPI.typeProductCommands.DeleteTypeProductCommand import DeleteTypeProductCommand
from consoleAPI.typeProductCommands.UpdateTypeProductCommand import UpdateTypeProductCommand
from consoleAPI.typeProductCommands.GetTypeProductByIdCommand import GetTypeProductByIdCommand
from consoleAPI.typeProductCommands.AddTypeProductCommand import AddTypeProductCommand

from consoleAPI.productCommands.DeleteProductCommand import DeleteProductCommand
from consoleAPI.productCommands.UpdateProductCommand import UpdateProductCommand
from consoleAPI.productCommands.GetProductByIdCommand import GetProductByIdCommand
from consoleAPI.productCommands.AddProductCommand import AddProductCommand

from consoleAPI.featuresCommand.CountProductsForEachColorCommand import CountProductsForEachColorCommand

from data.SQLiteConnector import SQLiteConnector
from data.repository.ColorRepository import ColorRepository
from data.repository.ProductRepository import ProductRepository
from data.repository.TypeProductRepository import TypeProductRepository
import csv


if __name__ == '__main__':
    DB_PATH = './Laba3/db/laba3_db.db'
    connector = SQLiteConnector(DB_PATH)
    colorRepo = ColorRepository(connector)
    typeProductRepo = TypeProductRepository(connector)
    productRepo = ProductRepository(connector)

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

        GetTypeProductByIdCommand(typeProductRepo),
        AddTypeProductCommand(typeProductRepo),
        DeleteTypeProductCommand(typeProductRepo),
        UpdateTypeProductCommand(typeProductRepo),

        GetProductByIdCommand(productRepo),        
        AddProductCommand(productRepo, colorRepo, typeProductRepo),
        DeleteProductCommand(productRepo),
        UpdateProductCommand(productRepo, colorRepo, typeProductRepo),

        CountProductsForEachColorCommand(connector)
    ]

    print('help - справка по всем коммандам')
    print('help [command] - справка по камманде')
    print('q - выход из программы')

    while True:
        print('> ', end='')
        parts = input().split(' ')

        if len(parts) == 0:
            print('Ошибка!!!')
            continue
        
        commandName = parts[0]

        if len(parts) == 1 and commandName == 'help':
            for command in commands: 
                print(command)
            continue

        if len(parts) == 2 and commandName == 'help':
            for command in filter(lambda command: command.name == parts[1], commands):
                print(command.help())
            continue
        
        if len(parts) == 1 and commandName == 'q':
            break

        filteredCommands = list(filter(lambda x: x.name == commandName, commands)) 

        if len(filteredCommands) == 0: 
            print('неизвестная комманда')
            continue

        command = filteredCommands[0] # type: BaseCommand
        command.handle(parts[1:])


