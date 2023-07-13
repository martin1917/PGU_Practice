from SingleVariableFunc import SingleVariableFunc
import math

class HyperbolicSine(SingleVariableFunc):
    def __init__(self):
        super().__init__(name='sinh(x)', desc='Гиперболический синус')

    def calc(self, x: float) -> float:
        return math.sinh(x)
    
    def getDerivative(self):
        return HyperbolicCosine()

    def getUsefulInfo(self) -> str:
        return 'Вид фунции sinh(x) = (exp(x) - exp(-x)) / 2'

    
class HyperbolicCosine(SingleVariableFunc):
    def __init__(self):
        super().__init__(name='cosh(x)', desc='Гиперболический косинус')

    def calc(self, x: float) -> float:
        return math.cosh(x)
    
    def getDerivative(self):
        return HyperbolicSine()

    def getUsefulInfo(self) -> str:
        return 'Вид фунции cosh(x) = (exp(x) + exp(-x)) / 2'