from SingleVariableFunc import SingleVariableFunc
import math


class Exponent(SingleVariableFunc):
    def __init__(self):
        super().__init__(name='exp(x)', desc='Экспонента')

    def calc(self, x: float) -> float:
        return math.exp(x)
    
    def getDerivative(self):
        return Exponent()