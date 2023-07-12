class TypeProduct:
    def __init__(self, typeName: str):
        self.id = -1
        self.typeName = typeName
    
    def __str__(self) -> str:
        s = f'id: {self.id};'
        s += f'название: {self.typeName};'
        return f'TypeProduct {{{s}}}'