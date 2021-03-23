### File: Class.py
### Classes defined: Class
from Attribute import Attribute
from Field import Field
from Method import Method

class Class():

        def __init__(self, name, xCor = -1, yCor = -1):
            self.name = name
            self.attributeDict = {}
            self.xCor = xCor
            self.yCor = yCor
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
        def addParameter(self, methodName, parameters, typ, name):
            if typ == "":
                raise KeyError(f'Type must be provided')
            if name == "":
                raise KeyError(f'Name must be provided')
            found = False
            methodIndex = 0                        
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == parameters:   
                    found = True              
                    methodIndex = i
                    break
            if not found:
                raise KeyError(f'Method {methodName} with parameters {parameters} not found')
            if (typ,name) in self.methodDict[methodName][methodIndex].parameters:
                raise KeyError(f'Parameter {name} already exists')
            # Check if adding the parameter causes identical method signatures (illegal)     
            testList = self.methodDict[methodName][methodIndex].parameters.copy()
            testList.append((typ, name))           
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == testList:   
                    raise KeyError(f'Adding \'{name}\' will cause a duplicate method signature.')
            # Finally, add the parameter
            self.methodDict[methodName][methodIndex].parameters.append((typ, name))

        def removeParameter(self, methodName, parameters, name):
            if name == "":
                raise KeyError(f'Name must be provided')
            # Check if method with given parameters exists (and get index)
            found = False
            methodIndex = 0
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == parameters:   
                    found = True
                    methodIndex = i
                    break        
            if not found:
                raise KeyError(f'Method {methodName} with parameters {parameters} not found')
            # Get the type of the parameter (not a parameter for simplicity)
            typ = ""
            found = False
            for tup in self.methodDict[methodName][methodIndex].parameters:
                if tup[1] == name:
                    typ = tup[0]
                    found = True
            if not found:
                raise KeyError(f'Parameter {name} does not belong to {methodName}')
            # Check if removing the parameter causes identical method signatures (illegal)
            testList = self.methodDict[methodName][methodIndex].parameters.copy()
            testList.remove((typ, name))           
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == testList:   
                    raise KeyError(f'Removing \'{name}\' will cause a duplicate method signature.')
            # Finally, remove the parameter
            self.methodDict[methodName][methodIndex].parameters.remove((typ, name))

        def removeAllParameters(self, methodName, parameters):
            # Check if method with given parameters exists (and get index)
            found = False
            methodIndex = 0
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == parameters:   
                    found = True
                    methodIndex = i
                    break       
            if not found:
                raise KeyError(f'Method {methodName} with parameters {parameters} not found')
            # Check if empty method signature already exists
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters  == []:
                    raise KeyError(f'Cannot remove all parameters because a method with an empty signature already exists')
            # Finally, remove all parameters
            self.methodDict[methodName][methodIndex].parameters.clear()

        def changeParameter(self, methodName, parameters, name, newType, newName):
            if name == "":
                raise KeyError(f'Name must be provided')
            if newType == "":
                raise KeyError(f'New type must be provided')
            if newName == "":
                raise KeyError(f'Name name must be provided')
            # Check if method with given signature exists
            found = False
            methodIndex = 0
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == parameters:   
                    found = True
                    methodIndex = i
                    break
            if not found:
                raise KeyError(f'Method {methodName} with parameters {parameters} not found')
            if (newType, newName) in self.methodDict[methodName][methodIndex].parameters:
                raise KeyError(f'Parameter {newName} already exists')
            # Append the new parameter (errors will be handled in addParameter)
            self.addParameter(methodName, parameters, newType, newName)
            # Remove the old parameter (errors will be handled in removeParameter)
            self.removeParameter(methodName, self.methodDict[methodName][methodIndex].parameters, name)

        def changeAllParameters(self, methodName, parameters, newParameters):
            # Check if method with given signature exists
            found = False
            methodIndex = 0
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters == parameters:   
                    found = True
                    methodIndex = i
                    break       
            if not found:
                raise KeyError(f'Method {methodName} with parameters {parameters} not found')
            # Check if changing all parameters causes duplicate method signatures.
            for i in range(len(self.methodDict[methodName])):
                if self.methodDict[methodName][i].parameters  == newParameters:
                    raise KeyError(f'Cannot change all parameters because a method with containing new parameter list already exists')
            # Clear the parameters
            self.methodDict[methodName][methodIndex].parameters.clear()
            # Add the new parameter list
            self.methodDict[methodName][methodIndex].parameters = newParameters

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

        # --------------------------- ( Coordinates ) ----------------------------- #
        def getX(self):
            return self.xCor

        def getY(self):
            return self.yCor

        def setX(self, X):
            self.xCor = X
            
        def setY(self, Y):
            self.yCor = Y
