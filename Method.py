'''
Filename: Method.py
Description: Stores information about a Class method including parameters and return types.
'''

class Method:
    def __init__(self, name, returnType, parameters=None):
        self.name = name
        self.returnType = returnType

        # TODO: parameter structure
        self.parameters = parameters
