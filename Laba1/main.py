from Product import Product


if __name__ == '__main__':
    # создание товаров
    cpu = Product()
    cpu.name = 'Процессор Intel Core i5 12400F, LGA 1700, OEM'
    cpu.priceInRuble = 15590
    cpu.manufacturer = 'Intel'

    motherboard = Product()
    motherboard.name = 'Материнская плата ASROCK B660 STEEL LEGEND, LGA 1700, Intel B660, ATX, Ret'
    motherboard.priceInRuble = 15360
    motherboard.manufacturer = 'ASROCK'

    print('Введите необходимые параметры для создание товара:')

    phone = Product()
    phone.name = input('Название телефона: ')
    phone.priceInRuble = float(input('Цена (₽) телефона: '))
    phone.manufacturer = input('Изготовитель телефона: ')

    products = [cpu, motherboard, phone]

    print()

    # Вывод всех товаров
    print('Созданные товары:', '=' * 50, sep='\n')
    for product in products:
        print(product)
    print('=' * 50, '\n')

    # Вывод цен в евро для всех товаров
    print('Цены товаров в евро (€):', '=' * 50, sep='\n')
    for product in products:
        print(f'[{product.name}] = {product.recalcPriceToEuro()}€')
    print('=' * 50, '\n')

    INCREASE_VALUE_IN_EURO = 50

    # Увеличение цены для Sumsung'ов
    for product in products:
        product.increasePriceForSamsung(INCREASE_VALUE_IN_EURO)

    # Вывод цен в евро после увеличение цен
    print(f'Цены товаров в евро (€) после увелечение цены Sumsung\'ов на {INCREASE_VALUE_IN_EURO}€:', '=' * 50, sep='\n')
    for product in products:
        print(f'[{product.name}] = {product.recalcPriceToEuro()}€')
    print('=' * 50, '\n')