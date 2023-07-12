class Color:
    def __init__(self, colorName: str):
        self.id = -1
        self.colorName = colorName
    
    def __str__(self) -> str:
        s = f'id: {self.id};'
        s += f'название: {self.colorName};'
        return f'Color {{{s}}}'