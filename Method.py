'''
Filename: Method.py
Description: Stores information about a Class method including parameters and return types.
'''

class Method:
    def __init__(self, name, returnType, parameters=None):
        self.name = name
        self.returnType = returnType

        # parameter structure
        # [(retType1, name1), (retType2, name2), ...]
        self.parameters = parameters
