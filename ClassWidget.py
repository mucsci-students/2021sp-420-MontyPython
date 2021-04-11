from tkinter import *

class ClassWidget(Frame):
    def __init__(self, parent, canvas, txt, x, y):
        Frame.__init__(self, parent)

        # Canvas in GUIMainWindow
        self.canvas = canvas
        # Class widget width
        self.width = 0
        self.nameTxt = txt
        self.x = x
        self.y = y

        # List containing Lists of coordinate pairs for drawing relationships. Ex: [[x1, y1], [x2, y2], [x3, y3]]
        self.widgetCoordinates = []
        # Contains objects NameText, NameBox, FieldText, FieldBox, MethodText, MethodBox
        self.objectDict = {}

        # Create the three text boxes
        self.initText()

        # Update where text boxes show up on the GUI based on text contents
        self.updateWidget()

    # ------------------------------------------------------------- #
    #                Initial text and box creation
    # ------------------------------------------------------------- #

    # Create name, field, and method text
    def initText(self):
        self.createText(self.x, self.y, "Name", self.nameTxt)
        self.createText(0, 0, "Field", "")
        self.createText(0, 0, "Method", "")

    # Identifier = Name, Field, or Method
    def createText(self, x, y, identifier, txt):
        self.objectDict[identifier + "Text"] = self.canvas.create_text(x, y, text=txt, fill="black", anchor = 'nw', tag=self.nameTxt)

    # Creates boxes that go around text
    def drawBoxes(self):
        self.drawBox("Name", self.getNameObject())
        self.drawBox("Field", self.getFieldObject())
        self.drawBox("Method", self.getMethodObject())

    # Identifier = Name, Field, or Method; txtBoxObj = objectDict entry
    def drawBox(self, identifier, txtBoxObj):
        # bbox returns a list [x1, y1, x2, y2]
        boundingBox = self.canvas.bbox(txtBoxObj)

        # Create the actual box. (x1, y1) top left corner, (x2, y2) bottom right corner
        self.objectDict[identifier + "Box"] = self.canvas.create_rectangle(boundingBox[0], boundingBox[1], (boundingBox[0] + self.width), boundingBox[3], outline="black", fill="white", tag=self.nameTxt)
       
        # Moves items up to be in front of other objects
        self.canvas.tag_raise(self.objectDict[identifier + "Box"])
        self.canvas.tag_raise(self.objectDict[identifier + "Text"])

    # ------------------------------------------------------------- #
    #                Methods for updating widget
    # ------------------------------------------------------------- #

    # Runs methods that update the location/sizes of the boxes based on the contents
    def updateWidget(self):
        # Find the longest text box so all widths can match it
        self.updateWidth()
        # Move the boxes to appear on top of eachother
        self.updateTextLocations()
        # Draws the actual boxes around the text
        self.delAndRedrawBoxes()
        # Update the coordiante list for relationships
        self.updateCoordinateList()

    def delAndRedrawBoxes(self):
        self.deleteBoxesFromCanvas()
        self.drawBoxes()
    
    # Finds the box with the longest width so they can all be set to that width
    def updateWidth(self):
        # Get widths
        nameWidth = self.getNameWidth()
        fieldWidth = self.getFieldWidth()
        methodWidth = self.getMethodWidth()

        # Method is largest
        if methodWidth > fieldWidth and methodWidth > nameWidth:
            w = methodWidth
        # Field is largest
        elif fieldWidth > methodWidth and fieldWidth > nameWidth:
            w = fieldWidth
        # Name is largest
        elif nameWidth > fieldWidth and nameWidth > methodWidth:
            w = nameWidth
        # They're all the same
        else:
            w = nameWidth
        
        self.width = w
        
    # Shifts the three individual boxes together to look like one box
    def updateTextLocations(self):
        nameHeight = self.getNameHeight()
        fieldHeight = self.getFieldHeight()

        # Coords for the top left corner of the boxes
        nameCoords = [self.getNameCoords()[0], self.getNameCoords()[1]]

        # Coordinates are based around the top left corner of the name box
        newFieldY = self.getNameCoords()[1] + nameHeight
        newMethodY = self.getNameCoords()[1] + nameHeight + fieldHeight

        self.canvas.coords(self.getFieldObject(), self.getNameCoords()[0], newFieldY)
        self.canvas.coords(self.getMethodObject(), self.getNameCoords()[0], newMethodY)

    # Updates/adds coordinates in widgetCoordinates
    def updateCoordinateList(self):
        # If the list has elements, delete all elements
        if self.widgetCoordinates:
            self.widgetCoordinates.clear()

        nameCoords = self.getNameBoxCoords()
        methodCoords = self.getMethodBoxCoords()

        # Mid points (in order): Top middle [0], Left middle [1], Right middle [2], Bottom middle [3]
        self.widgetCoordinates.append([((nameCoords[0] + nameCoords[2]) / 2), nameCoords[1]])
        self.widgetCoordinates.append([nameCoords[0], ((nameCoords[1] + methodCoords[3]) / 2)])
        self.widgetCoordinates.append([methodCoords[2], ((nameCoords[1] + methodCoords[3]) / 2)])
        self.widgetCoordinates.append([((methodCoords[0] + methodCoords[2]) / 2), methodCoords[3]])

        # Corners (in order): Top left [4], Top right [5], Bottom left [6], Bottom right [7]
        self.widgetCoordinates.append([nameCoords[0], nameCoords[1] + 5])
        self.widgetCoordinates.append([nameCoords[2], nameCoords[1] + 5])
        self.widgetCoordinates.append([methodCoords[0], methodCoords[3] - 5])
        self.widgetCoordinates.append([methodCoords[2], methodCoords[3] - 5])

    # ------------------------------------------------------------- #
    #          Methods that delete objects from dict/canvas
    # ------------------------------------------------------------- #
    def deleteBoxesFromCanvas(self):
        if "NameBox" in self.objectDict:
            nameBox = self.getNameBoxObject()
            fieldBox = self.getFieldBoxObject()
            methodBox = self.getMethodBoxObject()

            self.canvas.delete(nameBox)
            self.canvas.delete(fieldBox)
            self.canvas.delete(methodBox)

            del nameBox
            del fieldBox
            del methodBox

    def deleteTextFromCanvas(self):
        if "NameText" in self.objectDict:
            nameTxt = self.getNameObject()
            fieldTxt = self.getFieldObject()
            methodTxt = self.getMethodObject()

            self.canvas.delete(nameTxt)
            self.canvas.delete(fieldTxt)
            self.canvas.delete(methodTxt)
            
            del nameTxt
            del fieldTxt
            del methodTxt

    # If you call this, be sure to also delete the widget from whatever dict it is stored in
    def deleteWidgetFromCanvas(self):
        self.deleteBoxesFromCanvas()
        self.deleteTextFromCanvas()

    # ------------------------------------------------------------- #
    #                         Set text
    # ------------------------------------------------------------- #
    
    def setNameText(self, txt):
        self.canvas.itemconfig(self.getNameObject(), text=txt)
        self.updateWidget()

    def setFieldText(self, txt):
        self.canvas.itemconfig(self.getFieldObject(), text=txt)
        self.updateWidget()

    def setMethodText(self, txt):
        self.canvas.itemconfig(self.getMethodObject(), text=txt)
        self.updateWidget()

    # ------------------------------------------------------------- #
    #                  Get objects in objectDict
    # ------------------------------------------------------------- #

    def getNameObject(self):  
        return self.objectDict["NameText"]
    
    def getFieldObject(self):
        return self.objectDict["FieldText"]
    
    def getMethodObject(self):
        return self.objectDict["MethodText"]

    def getNameBoxObject(self):  
        return self.objectDict["NameBox"]
    
    def getFieldBoxObject(self):
        return self.objectDict["FieldBox"]
    
    def getMethodBoxObject(self):
        return self.objectDict["MethodBox"]

    # ------------------------------------------------------------- #
    #                       Get Coordinates
    # ------------------------------------------------------------- #
    
    # getNameCoords, getFieldCoords, and getMethodCoords return the coordinates for the top left corner of the box
    def getNameCoords(self):
        return self.canvas.coords(self.getNameObject())

    def getFieldCoords(self):
        return self.canvas.coords(self.getFieldObject())

    def getMethodCoords(self):
        return self.canvas.coords(self.getMethodObject())

    def getNameBoxCoords(self):
        return self.canvas.coords(self.getNameBoxObject())
    
    def getFieldBoxCoords(self):
        return self.canvas.coords(self.getFieldBoxObject())

    def getMethodBoxCoords(self):
        return self.canvas.coords(self.getMethodBoxObject())

    # Returns a list of two coordinates for the top left corner of the widget. [x, y]
    def getWidgetCoords(self):
        return self.getNameCoords()

    # ------------------------------------------------------------- #
    #                    Get widths and heights
    # ------------------------------------------------------------- #

    def getNameWidth(self):
        nameBoundingBox = self.canvas.bbox(self.getNameObject())
        return nameBoundingBox[2] - nameBoundingBox[0]

    def getFieldWidth(self):
        fieldBoundingBox = self.canvas.bbox(self.getFieldObject())
        return fieldBoundingBox[2] - fieldBoundingBox[0]

    def getMethodWidth(self):
        methodBoundingBox = self.canvas.bbox(self.getMethodObject())
        return methodBoundingBox[2] - methodBoundingBox[0]

    def getNameHeight(self):
        nameCoords = self.canvas.bbox(self.getNameObject())
        return nameCoords[3] - nameCoords[1]

    def getFieldHeight(self):
        fieldCoords = self.canvas.bbox(self.getFieldObject())
        return fieldCoords[3] - fieldCoords[1]

    def getMethodHeight(self):
        methodCoords = self.canvas.bbox(self.getMethodObject())
        return methodCoords[3] - methodCoords[1]

    # ------------------------------------------------------------- #
    #                       Helper methods
    # ------------------------------------------------------------- #

    # Draws a circle at each widget coordinate location for debugging purposes
    def circleTest(self):
        for c in self.widgetCoordinates:
            self.createCircle(c[0], c[1])
            print(c[0], c[1])

    def createCircle(self, x, y):
        x1 = x - 5
        y1 = y - 5
        x2 = x + 5
        y2 = y + 5
        self.canvas.tag_raise(self.canvas.create_oval(x1, y1, x2, y2, fill="blue"))


