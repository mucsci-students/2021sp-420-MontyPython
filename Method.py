'''
Filename: Method.py
Description: Stores information about a Class method including parameters and return types.
'''

class Method:
    def __init__(self, name, returnType, parameters):
        self.name = name
        self.returnType = returnType

        # parameter structure
        # [(retType1, name1), (retType2, name2), ...]
        self.parameters = parameters.copy()
    def __repr__(self):
        if len(self.parameters) > 0:
            paramStr = ''
            for param in self.parameters:
                paramStr += f'{param[0]} {param[1]}, '
            return f'{self.returnType} {self.name}({paramStr[:-2]})'
        else:
            return f'{self.returnType} {self.name}()'
    def __str__(self):
        return self.__repr__()
