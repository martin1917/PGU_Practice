class Product:
    EURO_RATE = 100.42

    def __init__(self):
        self.name = ''
        """наименование товара"""
        self.priceInRuble = 0.00
        """цена товара в рублях"""
        self.manufacturer = ''
        """изготовитель товара"""

    def recalcPriceToEuro(self) -> float:
        """Пересчитать цену товара в евро"""
        return round(self.priceInRuble / Product.EURO_RATE, 2)
    
    def increasePriceForSamsung(self, moneyInEuro: float):
        """
            Увеличить цену товара в евро, 
            если название товара содержит 
            слово «Samsung».

            Параметры:
                moneyInEuro (float): сумма в евро, на которую нужно увеличить
        """
        if 'Samsung' in self.name:
            self.priceInRuble += moneyInEuro * Product.EURO_RATE

    def __str__(self) -> str:
        nameStr = f'Товар: {self.name};'
        priceStr = f'Цена: {self.priceInRuble}₽;'
        manufacturerStr = f'Изготовитель: {self.manufacturer}'
        return f'{{{nameStr} {priceStr} {manufacturerStr}}}'
    
    def __del__(self):
        print(f'Товар [{self.name}] УНИЧТОЖЕН !!!')