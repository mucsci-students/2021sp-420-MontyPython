### File: Class.py
### Classes defined: Class
from Attribute import Attribute
from Field import Field
from Method import Method

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
            if name not in self.methodDict:
                self.methodDict[name] = []
            for m in self.methodDict[name]:
                if m.parameters == parameters:
                    raise KeyError(f"Cannot add method {name}. Method {name} already exists with parameters {parameters}")
            self.methodDict[name].append(Method(name, returnType, parameters))

        def deleteMethod(self, name, parameters):
            if name not in self.methodDict:
                raise KeyError(f"Cannot delete method {name}. Method {name} does not exist in class {self.name}")
            found = False
            for i in range(len(self.methodDict[name])):
                if self.methodDict[name][i].parameters == parameters:
                    self.methodDict[name].pop(i)
                    found = True
                    break

            if not found:
                raise KeyError(f"Cannot delete method {name}. Method {name} does not exist with parameters {parameters}")
            if len(self.methodDict[name]) == 0:
                del self.methodDict[name]
        def renameMethod(self, oldName, parameters, newName):
            if oldName not in self.methodDict:
                raise KeyError(f"Method {oldName} does not exist in class {self.name}")
            found = False
            methodIndex = 0
            # Check to see method with these parameters exists
            for i in range(len(self.methodDict[oldName])):
                if self.methodDict[oldName][i].parameters == parameters:
                    # self.methodDict[oldName].pop(i)
                    methodIndex = i
                    found = True
                    break
            if not found:
                raise KeyError(f"Cannot rename method {oldName}. Method {oldName} does not exist with parameters {parameters}")
            # Try to add method with newName BEFORE removing oldName instance just in case newName already exists.
            try:
                returnType = self.methodDict[oldName][methodIndex].returnType
                self.addMethod(newName, returnType, parameters)
            except KeyError:
                raise KeyError(f"Cannot rename method {oldName}. Method {newName} already exists with parameters {parameters}")
            
            self.deleteMethod(oldName, parameters)

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
