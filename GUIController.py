import sys
from ClassCollection import ClassCollection
import Interface
from PopupBoxes import *
import GUIMenuBar

# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.root = self.view.master

        # Creates the view's menu bar
        self.createMenuBar()

        # Jen note: This was old sprint 2 code but I might need it for sprint 3 stuff, so I kept it for now. 
        # -------------------------------------------------- * 
        self.coordinateList = [[50, 100], [50, 400], [400, 100], [400, 400], [750, 100], [750, 400], [50, 750], [400, 750], [750, 750]]
        #self.unusedGridList = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
        self.usedGridDict = {}
        #self.classWidgetDict = {}
        # Update this when classes are added/removed to get the correct coordinates
        # TODO: throw an error if user tries to add more than 9 classes. Say only 9 can be displayed
        self.classWidgetCount = 0
        # -------------------------------------------------- * 

    def open(self):
        pass

    def save(name):
        pass

    def help(self):
        pass

    def exit(self):
        sys.exit()

    def addClass(self, name):
        if name == '':
            alertBox = self.windowFactory("alertBox", "Please provide a class name")
            return

        try:
            self.model.addClass(name)
            coordinates = self.coordinateList[self.classWidgetCount]
            self.view.addClass(name, coordinates[0], coordinates[1])
            self.classWidgetCount = self.classWidgetCount + 1
            
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)
     
    def deleteClass(self, name):
        if name == '':
            alertBox = self.windowFactory("alertBox", "Please provide a class name")
            return

        try:
            self.model.deleteClass(name)

        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)       

        print(self.model.classDict)
        
    def renameClass(self, oldName, newName):
        errorFlag = False
        errorString = ''

        if oldName == '':
            errorFlag = True
            errorString += '\nPlease provide a class name'
        
        if newName == '':
            errorFlag = True
            errorString += '\nPlease provide a new class name'
        
        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.renameClass(oldName, newName)

        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def addRelationship(self, firstClassName, secondClassName, typ):
        errorFlag = False
        errorString = ''
       
        if firstClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a first class name'
        
        if secondClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a second class name'

        if typ == -1:
            errorFlag = True
            errorString += '\nPlease provide a type name'

        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return
        
        try:
            self.model.addRelationship(firstClassName, secondClassName, typ)

        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.relationshipDict)

    def deleteRelationship(self, firstClassName, secondClassName):
        errorFlag = False
        errorString = ''
    
        if firstClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a first class name'
        
        if secondClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a second class name'

        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.deleteRelationship(firstClassName, secondClassName)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.relationshipDict)

    def renameRelationship(self, firstClassName, secondClassName, typ):
        errorFlag = False
        errorString = ''
    
        if firstClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a first class name'
        
        if secondClassName == '':
            errorFlag = True
            errorString += '\nPlease provide a second class name'

        if typ == -1:
            errorFlag = True
            errorString += '\nPlease provide a type name'

        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.renameRelationship(firstClassName, secondClassName, typ)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.relationshipDict)

    def addMethod(self, className, methodName, returnType, parameters):
        try:
            self.model.addMethod(className, methodName, returnType, parameters)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict[className].methodDict)

    def deleteMethod(self, className, methodName, methodNum):
        try:
            idx = int(methodNum) - 1
            params = self.model.getMethod(className, methodName, idx).parameters
            self.model.deleteMethod(className, methodName, params)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)    

    def renameMethod(self, className, methodName, methodNum, newName):
        try:
            idx = int(methodNum) - 1
            params = self.model.getMethod(className, methodNum, idx).parameters
            self.model.renameMethod(className, methodName, params, newName)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def addParameter(self, className, methodName, methodNum, typ, name):
        try:
            idx = int(methodNum) - 1
            params = self.model.getMethod(className, methodNum, idx).parameters
            self.model.addParameter(className, methodName, params, typ, name)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)
        
        print(self.model.classDict)

    def removeParameter(self, className, methodName, methodNum, name):
        try:
            idx = int(methodNum) - 1
            params = self.model.getMethod(className, methodNum, idx).parameters
            self.model.removeParameter(className, methodName, params, name)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def changeParameter(self, className, methodName, methodNum, name, newType, newName):
        try:
            idx = int(methodNum) - 1
            params = self.model.getMethod(className, methodNum, idx).parameters
            self.model.changeParameter(className, methodName, params, name, newType, newName)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def addField(self, className, name, dataType):
        errorFlag = False
        errorString = ''

        if className == '':
            errorFlag = True
            errorString += '\nPlease provide a class name'

        if name == '':
            errorFlag = True
            errorString += '\nPlease provide a field name'
        
        if dataType == '':
            errorFlag = True
            errorString += '\nPlease provide a datatype'
        
        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.addField(className, name, dataType)

            self.view.classWidgetDict[className].setField(newName)
            
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def deleteField(self, className, name):
        errorFlag = False
        errorString = ''

        if className == '':
            errorFlag = True
            errorString += '\nPlease provide a class name'

        if name == '':
            errorFlag = True
            errorString += '\nPlease provide a field name'
        
        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.deleteField(className, name)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)

    def renameField(self, className, oldName, newName):
        errorFlag = False
        errorString = ''

        if className == '':
            errorFlag = True
            errorString += '\nPlease provide a class name'

        if oldName == '':
            errorFlag = True
            errorString += '\nPlease provide a field name'

        if newName == '':
            errorFlag = True
            errorString += '\nPlease provide a new field name'
        
        if errorFlag:
            alertBox = self.windowFactory("alertBox", errorString)
            return

        try:
            self.model.renameField(className, oldName, newName)
        except Exception as e:
            errorBox = self.windowFactory("alertBox", e)

        print(self.model.classDict)
    
    def listMethods(self, className, methodName, numbered=True):
        if className in self.model.classDict and methodName in self.model.getAllMethods(className):
            methods = self.model.getMethodsByName(className, methodName)
            if not numbered:
                return '\n'.join(map(str, methods))
            else:
                lstStr = ''
                for i in range(len(methods)):
                    lstStr += f'{i+1}. {methods[i]}'
                return lstStr.strip()
        return ''
    
    def getClasses(self):
        return list(self.model.classDict.keys())

    # --------------------------------
    # Menu Methods
    # --------------------------------

    def createMenuBar(self):
        GUIMenuBar.menu(self, self.view, self.root)

    # Create a window using the factory method
    def windowFactory(self, windowType = "alertBox", errorMsg = ""):
    
        windows = {
            "alertBox": AlertBox,
            "Add Class": AddClassBox,
            "Delete Class": DeleteClassBox,
            "Rename Class": RenameClassBox,
            "Add Field": AddFieldBox,
            "Delete Field": DeleteFieldBox,
            "Rename Field": RenameFieldBox,
            "Add Method": AddMethodBox,
            "Delete Method": DeleteMethodBox,
            "Rename Method": RenameMethodBox,
            "Add Parameter": AddParameterBox,
            "Delete Parameter": DeleteParameterBox,
            "Change Parameter": ChangeParameterBox,
            "Add Relationship": AddRelationshipBox,
            "Delete Relationship": DeleteRelationshipBox,
            "Change Relationship": ChangeRelationshipBox
        }
        
        # Show window
        box = windows[windowType](windowType, errorMsg, self)

    