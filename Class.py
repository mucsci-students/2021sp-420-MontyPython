### File: Class.py
### Classes defined: Class
from Attribute import Attribute
from Field import Field

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
        # MethodDict structure
        #     ('name'): {'feildObject'}
            self.fieldDict = {}
        
        def rename(self, newName):
            self.name = newName
        
        # --------------------------- ( Method ) ----------------------------- #
        def addMethod(self, name, returnType):
            pass

        def deleteMethod(self, name, returnType, parameters):
            pass
        
        def renameMethod(self, name, returnType, parameters, newName):
            pass

        # ----------------------------( Parameters ) ------------------------ #
        def addParameter(self, method, paramList, type, name):
            pass

        def removeParameter(self, method, paramList, type, name):
            pass

        def changeParameter(self, method, paramList, type, name, newName):
            pass

        # --------------------------- ( Field ) ----------------------------- #
        def addField(self, name, dataType):
            if name in self.fieldDict:
                raise KeyError(f"{name} is already an field")
            self.fieldDict[name] = Field(name, dataType)

        def deleteField(self, name):
            if name not in self.fieldDict:
                raise KeyError(f"{name} is not an field for {self.name}")
            del self.fieldDict[name]
        
        def renameField(self, oldName, newName):
            if oldName not in self.fieldDict:
                raise KeyError(f"{oldName} is not a field for {self.name}")
            if newName in self.fieldDict:
                raise KeyError(f"{newName} is already a field for {self.name}")
            self.fieldDict[newName] = self.fieldDict.pop(oldName)

        def getField(self, name):
            if name not in self.fieldDict:
                raise KeyError(f"{name} is not an field for {self.name}")
            return self.fieldDict[name]

        # --------------------------- ( Attribute ) ----------------------------- #
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
