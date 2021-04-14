import sys
from ClassCollection import ClassCollection
import Interface
from PopupBoxes import *
import GUIMenuBar
import traceback

# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model, view, debug):
        self.model = model
        self.view = view
        self.root = self.view.master
        self.debug = debug
        # Creates the view's menu bar
        self.createMenuBar()

        # TODO: Delete this and related code once classes can move
        self.coordinateList = [[50, 100], [50, 400], [400, 100], [400, 400], [750, 100], [750, 400], [50, 750], [400, 750], [750, 750]]
        self.usedCoordinateDict = {}
        self.classWidgetCount = 0


    def load(self, name):
        if self.debug:
            print(name)
        Interface.loadFile(self.model, name, "GUI", self.view)
         #self.view.drawLines()

    def save(self, name):
        Interface.saveFile(self.model, name, "GUI", self.view)

    def help(self):
        pass

    def exit(self):
        sys.exit()

    def addClass(self, name):
        if name == '':
            alertBox = self.windowFactory("alertBox", "Please provide a class name")
            return

        # TODO: Once classes are able to be moved, remove this
        if self.classWidgetCount == 9:
            alertBox = self.windowFactory("alertBox", "Only 9 classes are able to be added to the GUI verison of this program.")
            return

        try:
            self.model.addClass(name)
            # Update number of widgets on screen
            self.classWidgetCount = self.classWidgetCount + 1
            # Get the coordinates from the coordinateList at index 0
            coordinates = self.coordinateList[0]
            # Add class based on thoes coordinates
            self.view.addClass(name, coordinates[0], coordinates[1])
            # Move those coordinates to the used coordinate dict, remove them from the normal coordinate list
            self.usedCoordinateDict[name] = coordinates
            self.coordinateList.remove(coordinates)
            
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)

        if self.debug:
            print(self.model.classDict)
     
    def deleteClass(self, name):
        if name == '':
            alertBox = self.windowFactory("alertBox", "Please provide a class name")
            return

        try:
            self.model.deleteClass(name)
            # Remove the class from the view
            self.view.deleteClass(name)
            # Update number of classes on screen
            self.classWidgetCount = self.classWidgetCount - 1
            # Remove coords from used coord dict, add back to coordinate list
            coords = self.usedCoordinateDict.pop(name)
            self.coordinateList.append(coords)

        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)       
        if self.debug:
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

            # Update view
            self.view.classDict[oldName].setNameText(newName)
            self.view.classDict[oldName].updateWidget()
            self.view.classDict[newName] = self.view.classDict.pop(oldName)

            # Change coordinate dict name to match new class name
            coords = self.usedCoordinateDict.pop(oldName)
            self.usedCoordinateDict[newName] = coords
            self.view.renameClass(oldName, newName)

        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)

        if self.debug:
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
            self.view.addLine(firstClassName, secondClassName, typ)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
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
            self.view.deleteLine(firstClassName, secondClassName)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
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
            self.view.renameLine(firstClassName, secondClassName, typ)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.relationshipDict)

    def addMethod(self, className, methodName, returnType, parameters):
        try:
            self.model.addMethod(className, methodName, returnType, parameters)
            self.updateWidgetMethod(className)

        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict[className].methodDict)

    def deleteMethod(self, className, methodName, params):
        try:
            self.model.deleteMethod(className, methodName, params)
            self.updateWidgetMethod(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict)    

    def renameMethod(self, className, methodName, params, newName):
        try:
            self.model.renameMethod(className, methodName, params, newName)
            self.updateWidgetMethod(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict)

    def addParameter(self, className, methodName, params, typ, name):
        try:
            self.model.addParameter(className, methodName, params, typ, name)
            self.updateWidgetMethod(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict[className].methodDict)

    def removeParameter(self, className, methodName, params, name):
        try:
            self.model.removeParameter(className, methodName, params, name)
            self.updateWidgetMethod(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict)

    def changeParameter(self, className, methodName, params, name, newType, newName):
        try:
            self.model.changeParameter(className, methodName, params, name, newType, newName)
            self.updateWidgetMethod(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
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
            self.updateWidgetField(className)
            
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
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
            self.updateWidgetField(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
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
            self.updateWidgetField(className)
        except Exception as e:
            if self.debug:
                print(traceback.format_exc())
            errorBox = self.windowFactory("alertBox", e)
        if self.debug:
            print(self.model.classDict)
    
    def listMethods(self, className, methodName, numbered=True):
        if className in self.model.classDict and methodName in self.model.getAllMethods(className):
            methods = self.model.getMethodsByName(className, methodName)
            if not numbered:
                return '\n'.join(map(str, methods))
            else:
                lstStr = ''
                for i in range(len(methods)):
                    lstStr += f'{i+1}. {methods[i]}\n'
                return lstStr.rstrip()
        return ''
    
    def getClasses(self):
        return list(self.model.classDict.keys())
    
    def getFields(self, className):
        return list(self.model.getFields(className))
    
    def getMethodsByName(self, className, methodName):
        return list(self.model.getMethodsByName(className, methodName))
    
    def getAllMethodsString(self, className):
        names = self.model.getAllMethods(className)
        lst = []
        for name in names:
            for method in self.model.getMethodsByName(className, name):
                lst.append(method)
        return lst


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
            "Change Relationship": ChangeRelationshipBox,
            "Save": SaveBox,
            "Open": LoadBox,
            "Help": HelpBox
        }
        
        # Show window

        box = windows[windowType](windowType, errorMsg, self)

    # --------------------------------
    # Update Methods
    # --------------------------------

    def updateWidgetField(self, className):
        fieldStr = ""
        for field in self.model.getFields(className).values():
            fieldStr += f'{field}\n'
        fieldStr = fieldStr.rstrip()
        size = len(fieldStr)
        self.view.classDict[className].setFieldText(fieldStr)

    def updateWidgetMethod(self, className):
        methodStr = ""
        for methodList in self.model.getAllMethods(className).values():
            for method in methodList:
                methodStr += f'{method}\n'
        size = len(methodStr)
        methodStr = methodStr.rstrip()
        self.view.classDict[className].setMethodText(methodStr)  

