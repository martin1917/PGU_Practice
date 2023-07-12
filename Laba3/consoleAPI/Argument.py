class Argument:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
    
    def __str__(self) -> str:
        return f'{self.name} - {self.description}'