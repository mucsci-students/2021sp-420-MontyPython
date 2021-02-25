### File: Class.py
### Classes defined: Class
from Attribute import Attribute
from Field import Field

class Class():

        def __init__(self, name):
            self.name = name
            self.attributeDict = {}
        
        # methodDict structure
        #     'methodName1': [method1, method2, ...]
            self.methodDict = {}
        # fieldDict structure
        #     ('name'): {'feildObject'}
            self.fieldDict = {}
        
        def rename(self, newName):
            self.name = newName
        
        # --------------------------- ( Method ) ----------------------------- #
        def addMethod(self, name, returnType, parameters = []):
            pass

        def deleteMethod(self, name, parameters):
            pass
        
        def renameMethod(self, oldName, parameters, newName):
            pass

        # ----------------------------( Parameters ) ------------------------ #
        def addParameter(self, methodName, parameters, type, name):
            pass

        def removeParameter(self, methodName, parameters, name):
            pass

        def removeAllParameters(self, methodName, parameters):
            pass

        def changeParameter(self, methodName, parameters, name, newType, newName):
            pass

        def changeAllParameters(self, methodName, parameters, newParameters):
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
