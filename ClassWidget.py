from tkinter import *

class ClassWidget(Frame):
    def __init__(self, parent, canvas):
        Frame.__init__(self, parent)

        # The canvas in the main window
        self.canvas = canvas

        # Text width, all will be set to the same number
        self.width = 0

        # Contains objects NameText, NameBox, FieldText, FieldBox, MethodText, MethodBox
        self.objectDict = {}

        # Creates the text boxes. Everything is based around these
        self.initText()

        # Gets default coordiantes of the name, field, and method text box to use in other methods [x1, y1, x2, y2]
        self.nameBoundingBox = self.canvas.bbox(self.getNameObject())
        self.fieldBoundingBox = self.canvas.bbox(self.getFieldObject())
        self.methodBoundingBox = self.canvas.bbox(self.getMethodObject())

        # Update where text boxes show up on the GUI based on text contents
        self.updateWidget()

    # --------------------------------------------------- #
    # Methods that only run when a new widget is made
    # --------------------------------------------------- #

    # Create three text items
    def initText(self):
        self.createText(200, 200, "Name", "Name")
        self.createText(200, 300, "Field", "Field")
        self.createText(200, 400, "Method", "Method")

    # Creates the text for the text box. 
    # x, y = coordinates; Identifier = Name, Field, or Method; Txt = the text to go inside the box
    def createText(self, x, y, identifier, txt):
        # create_text(x, y, options ...)
        # Anchor info: https://www.tutorialspoint.com/python/tk_anchors.htm
        self.objectDict[identifier + "Text"] = self.canvas.create_text(x, y, text=txt, fill="black", anchor = 'nw')


    # --------------------------------------------------- #
    # Methods that update the text and box locations
    # --------------------------------------------------- #

    # Runs methods that update the location/sizes of the boxes based on the contents
    def updateWidget(self):
        # Set widths of all boxes to match the largest one
        self.setTextWidths()
        # Move the boxes to appear on top of eachother
        self.updateTextLocations()
        # Draws the actual boxes around the text
        self.updateBoxes()
        # Update bounding boxes incase they've changed
        self.updateBoundingBoxes()

    # Delete & Redraw
    def updateBoxes(self):
        self.deleteBoxesFromCanvas()
        self.drawBoxes()

    def drawBoxes(self):
        self.drawBox("Name", self.getNameObject())
        self.drawBox("Field", self.getFieldObject())
        self.drawBox("Method", self.getMethodObject())

    # Creates box that goes around text.
    # Identifier = Name, Field, or Method; txtBox = objectDict entry
    def drawBox(self, identifier, txtBox):
        # bbox returns a list [x1, y1, x2, y2]
        boundingBox = self.canvas.bbox(txtBox)

        # Create the actual box. create_rectangle: x1, y1, x2, y2, options.. (x1, y1) top left corner, (x2, y2) bottom right corner
        self.objectDict[identifier + "Box"] = self.canvas.create_rectangle(boundingBox[0], boundingBox[1], (boundingBox[0] + self.width), boundingBox[3], outline="black", fill="white")
       
        # Moves items up to be in front of other objects
        self.canvas.tag_raise(self.objectDict[identifier + "Box"])
        self.canvas.tag_raise(self.objectDict[identifier + "Text"])

        self.updateBoundingBoxes()

    # Needed for drawing boxes and moving the text
    def updateBoundingBoxes(self):
        self.nameBoundingBox = self.canvas.bbox(self.getNameObject())
        self.fieldBoundingBox = self.canvas.bbox(self.getFieldObject())
        self.methodBoundingBox = self.canvas.bbox(self.getMethodObject())
    
    # Finds the box with the largest width and sets all boxes to that width
    def setTextWidths(self):
        # Get widths
        nameWidth = self.getNameWidth()
        fieldWidth = self.getFieldWidth()
        methodWidth = self.getMethodWidth()

        # --- Find largest ---
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
            # TODO: This doesn't work correctly
            w = nameWidth

        # Update text with the new widths
        self.canvas.itemconfig(self.getNameObject(), width=w)
        self.canvas.itemconfig(self.getFieldObject(), width=w)
        self.canvas.itemconfig(self.getMethodObject(), width=w)

        self.updateBoundingBoxes()
        self.canvas.update()
        
        self.width = w

    # Shifts the three individual boxes together to look like one box
    def updateTextLocations(self):
        # Heights
        nameHeight = self.getNameHeight()
        fieldHeight = self.getFieldHeight()

        # Coords for the top left corner of the boxes
        nameCoords = self.getNameCoords()

        # Update the locations of the text boxes based on the heights
        newFieldY = nameCoords[1] + nameHeight
        newMethodY = nameCoords[1] + nameHeight + fieldHeight

        # Coordinates are based around the top left corner of the name box
        self.canvas.coords(self.getFieldObject(), nameCoords[0], newFieldY)
        self.canvas.coords(self.getMethodObject(), nameCoords[0], newMethodY)

    # --------------------------------------------------- #
    # Methods that delete objects from dict and canvas
    # --------------------------------------------------- #
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
            nametxt = self.getNameBoxObject()
            fieldTxt = self.getFieldBoxObject()
            methodTxt = self.getMethodBoxObject()

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

    # --------------------------------------------------- #
    # Setters for text
    # --------------------------------------------------- #
    
    def setNameText(self, txt):
        self.canvas.itemconfig(self.getNameObject(), text=txt)
        self.updateWidget()

    def setFieldText(self, txt):
        self.canvas.itemconfig(self.getFieldObject(), text=txt)
        self.updateWidget()

    def setMethodText(self, txt):
        self.canvas.itemconfig(self.getMethodObject(), text=txt)
        self.updateWidget()

    # --------------------------------------------------- #
    # Methods that return coordinates for the whole widget
    # --------------------------------------------------- #

    # TODO: Either do it this way, or create a list to iterate through to find shortest distance for relationships
    def widgetTopLeft(self):
        pass

    def widgetTopRight(self):
        pass

    def widgetBottomLeft(self):
        pass

    def widgetBottomRight(self):
        pass

    # Returns coordinates of top center in a list [x, y]
    def widgetTopMiddle(self):
        return [(nameBoundingBox[2] / 2), nameBoundingBox[1]]

    # Returns coordinates of bottom center in a list [x, y]
    def widgetBottomMiddle(self):
        #return []
        pass

    # Returns coordinates of left center in a list [x, y]
    def widgetLeftMiddle(self):
        #return []
        pass

    # Returns coordinates of right center in a list [x, y]
    def widgetRightMiddle(self):
        #return []
        pass

    def widgetMiddle(self):
        pass



    # --------------------------------------------------- #
    # Getters for each individual text box
    # --------------------------------------------------- #

    # Objects in dict
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
    
    # Coordinates of text
    def getNameCoords(self):
        return self.canvas.coords(self.getNameObject())

    def getFieldCoords(self):
        return self.canvas.coords(self.getFieldObject())

    def getMethodCoords(self):
        return self.canvas.coords(self.getMethodObject())

    # Width of each text
    def getNameWidth(self):
        return self.nameBoundingBox[2] - self.nameBoundingBox[0]

    def getFieldWidth(self):
        return self.fieldBoundingBox[2] - self.fieldBoundingBox[0]

    def getMethodWidth(self):
        return self.methodBoundingBox[2] - self.methodBoundingBox[0]

    # Height of each text
    def getNameHeight(self):
        return self.nameBoundingBox[3] - self.nameBoundingBox[1]

    def getFieldHeight(self):
        return self.fieldBoundingBox[3] - self.fieldBoundingBox[1]

    def getMethodHeight(self):
        return self.methodBoundingBox[3] - self.methodBoundingBox[1]


        # # TODO: Unfinished
        # for obj in self.objectDict:
        #     canvas.tag_bind(obj, '<Button1-Motion>', self.move)
        #     canvas.tag_bind(obj, '<ButtonRelease-1>', self.release)
        # self.clicked = False

    # # TODO: unfinished, still figuring this out
    # def move(self, event):
    #     if self.clicked:       
    #         self.canvas.move(obj, event.x - self.mouseX, event.y - self.mouseY)
    #         self.mouseX = event.x
    #         self.mouseY = event.y
    #     else:
    #         self.clicked = True
    #         self.canvas.tag_raise(obj)
    #         self.mouseX = event.x
    #         self.mouseY = event.y
 
    # def release(self, event):
    #     self.clicked = False
