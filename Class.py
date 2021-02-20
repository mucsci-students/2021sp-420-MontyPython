### File: Class.py
### Classes defined: Class
from Attribute import Attribute

class Class():

        def __init__(self, name):
            self.name = name
            self.attributeDict = {}
        
        # idea for methodDict structure
        # {
        #     ('age', 'int'): {'param1, param2, param3': methodObj1,
        #                      'param1, param2': methodObj2,
        #                      '': methodObj3
        #                     }
        # }
            self.methodDict = {}

        def rename(self, newName):
            self.name = newName
        
        def addMethod(self, name, returnType):
            pass

        def deleteMethod(self, name, returnType, parameters):
            pass
        
        def renameMethod(self, name, returnType, parameters, newName):
            pass

        def addAttribute(self, name):
            if name in self.attributeDict:
                raise KeyError(f"{name} is already an attribute for {self.name}")
            self.attributeDict[name] = Attribute(name)

        def deleteAttribute(self, name):
            if name not in self.attributeDict:
                raise KeyError(f"{name} is not an attribute for {self.name}")
            del self.attributeDict[name]

        def renameAttribute(self, oldName, newName):
            if oldName not in self.attributeDict:
                raise KeyError(f"{oldName} is not an attribute for {self.name}")
            self.attributeDict[newName] = self.attributeDict.pop(oldName)

        # Helper function for unit tests
        def getAttribute(self, name):
            if name not in self.attributeDict:
                raise KeyError(f"{name} is not an attribute for {self.name}")
            return self.attributeDict[name]

        # Helper function for unit tests
        def getAttributes(self):
            return self.attributeDict
