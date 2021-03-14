import sys
from ClassCollection import ClassCollection
import Interface


# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Jen note: This was old sprint 2 code but I might need it for sprint 3 stuff, so I kept it for now. 
        # -------------------------------------------------- * 
        #self.coordinateList = [[50, 100], [50, 400], [400, 100], [400, 400], [750, 100], [750, 400], [50, 750], [400, 750], [750, 750]]
        self.unusedGridList = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
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
        try:
            self.model.addClass(name)
            
        except Exception as e:
            print(e)

        print(self.model.classDict)
     
    def deleteClass(self, name):
        try:
            self.model.deleteClass(name)

        except Exception as e:
            print(e)
        

        print(self.model.classDict)
        
    def renameClass(self, oldName, newName):
        try:
            self.model.renameClass(oldName, newName)

        except Exception as e:
            print(e)

        print(self.model.classDict)

    def addRelationship(self, firstClassName, secondClassName, typ):
        try:
            self.model.addRelationship(firstClassName, secondClassName, typ)

        except Exception as e:
            print(e)

        print(self.model.relationshipDict)

    def deleteRelationship(self, firstClassName, secondClassName):
        try:
            self.model.deleteRelationship(firstClassName, secondClassName)
        except Exception as e:
            print(e)

        print(self.model.relationshipDict)

    def renameRelationship(self, firstClassName, secondClassName, typ):
        try:
            self.model.renameRelationship(firstClassName, secondClassName, typ)
        except Exception as e:
            print(e)

        print(self.model.relationshipDict)

    def addMethod(self, className, methodName, returnType, parameters):
        paramList = []
        try:
            for x in range(parameters.rowCount()):
                paramList.append((parameters.item(x,0).text(), parameters.item(x,1).text()))

            self.model.addMethod(className, methodName, returnType, paramList)
        except Exception as e:
            print(e)

        print(self.model.classDict[className].methodDict)

    def deleteMethod(self, className, methodName):
        try:
            self.model.deleteMethod(className, methodName)
        except Exception as e:
            print(e)

        print(self.model.classDict)    

    def renameMethod(self, className, methodName, newName):
        try:
            self.model.renameMethod(className, methodName, newName)
        except Exception as e:
            print(e)

        print(self.model.classDict)

    def addParameter(self, className, methodName, typ, name):
        try:
            self.model.addParameter(className, methodName, typ, name)
        except Exception as e:
            print(e)
        
        print(self.model.classDict)

    def removeParameter(self, className, methodName, name):
        try:
            self.model.removeParameter(className, methodName, name)
        except Exception as e:
            print(e)

        print(self.model.classDict)

    def changeParameter(self, className, methodName, name, newType, newName):
        try:
            self.model.changeParameter(className, methodName, name, newType, newName)
        except Exception as e:
            print(e)

        print(self.model.classDict)

    def addField(self, className, name, dataType):
        try:
            self.model.addField(className, name, dataType)

            self.view.classWidgetDict[className].setField(newName)
            
        except Exception as e:
            print(e)

        print(self.model.classDict)

    def deleteField(self, className, name):
        try:
            self.model.deleteField(className, name)
        except Exception as e:
            print(e)

        print(self.model.classDict)

    def renameField(self, className, oldName, newName):
        try:
            self.model.renameField(className, oldName, newName)
        except Exception as e:
            print(e)

        print(self.model.classDict)

