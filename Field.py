### File: Field.py
### Classes defined: Field
class Field:
    def __init__(self, name, dataType):
        self.name = name
        self.dataType = dataType
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f'{self.dataType} {self.name}'