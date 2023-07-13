from HyperbolicFunctions import HyperbolicSine, HyperbolicCosine
from Exponent import Exponent
from SingleVariableFunc import SingleVariableFunc


def calc(func: SingleVariableFunc, x: float):
    print(f'ФУНКЦИЯ: {func.name}\n')

    print(f'Значения в точке x = {x}', func.calc(x), sep='\n')
    print()

    dfunc = func.getDerivative() # type: SingleVariableFunc

    print(f'Производная функции: {dfunc.name}')
    print()

    print(f'Значения в точке x = {x} для функции производной', dfunc.calc(x), sep='\n')
    print()
    
    print('Полезная информация', func.getUsefulInfo(), sep='\n')

if __name__ == '__main__':
    x = 0.2

    sh = HyperbolicSine()
    calc(sh, x)

    print('*' * 75)

    ch = HyperbolicCosine()
    calc(ch, x)

    print('*' * 75)

    exp = Exponent()
    calc(exp, x)