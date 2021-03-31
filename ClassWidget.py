from tkinter import *

class ClassWidget(Frame):
    def __init__(self, parent, canvas, txt, x, y):
        Frame.__init__(self, parent)

        # The canvas in the main window
        self.canvas = canvas

        self.nameTxt = txt
        self.x = x
        self.y = y

        # List that contains lists of coordinate pairs that relationshpis can be drawn to
        # Ex: [[x1, y1], [x2, y2], [x3, y3]]
        self.widgetCoordinates = []

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
        self.createText(self.x, self.y, "Name", self.nameTxt)
        self.createText(0, 0, "Field", "")
        self.createText(0, 0, "Method", "")

    # Creates the text for the text box. 
    # x, y = coordinates; Identifier = Name, Field, or Method; Txt = the text to go inside the box
    def createText(self, x, y, identifier, txt):
        # create_text(x, y, options ...)
        # Anchor info: https://www.tutorialspoint.com/python/tk_anchors.htm
        self.objectDict[identifier + "Text"] = self.canvas.create_text(x, y, text=txt, fill="black", anchor = 'nw', tag=self.nameTxt)


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
        # Update the coordiante list for relationships
        self.updateCoordinateList()

        #self.circleTest()

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
        self.objectDict[identifier + "Box"] = self.canvas.create_rectangle(boundingBox[0], boundingBox[1], (boundingBox[0] + self.width), boundingBox[3], outline="black", fill="white", tag=self.nameTxt)
       
        # Moves items up to be in front of other objects
        self.canvas.tag_raise(self.objectDict[identifier + "Box"])
        self.canvas.tag_raise(self.objectDict[identifier + "Text"])


    # Needed for drawing boxes and moving the text
    # Bounding boxes changed to the actual box around the text after creation
    def updateBoundingBoxes(self):
        # self.nameBoundingBox = self.canvas.bbox(self.getNameObject())
        # self.fieldBoundingBox = self.canvas.bbox(self.getFieldObject())
        # self.methodBoundingBox = self.canvas.bbox(self.getMethodObject())
        self.nameBoundingBox = self.canvas.coords(self.getNameBoxObject())
        self.fieldBoundingBox = self.canvas.coords(self.getFieldBoxObject())
        self.methodBoundingBox = self.canvas.coords(self.getMethodBoxObject())
    
    # Finds the box with the largest width and sets all boxes to that width
    def setTextWidths(self):
        # The width never changes from the original one that the name is set through.
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
            w = nameWidth

        # Update text with the new widths
        # TODO This part doesn't work.
        #self.canvas.itemconfig(self.getNameObject(), width=w)
        #self.canvas.itemconfig(self.getFieldObject(), width=w)
        #self.canvas.itemconfig(self.getMethodObject(), width=w)
        self.canvas.update()
        
        self.width = w
        

    # Shifts the three individual boxes together to look like one box
    # TODO: Name's bounding box x1 and y1 is off here. 199 vs 200. Had to switch to using coords instead
    def updateTextLocations(self):
        # Heights
        nameHeight = self.getNameHeight()
        fieldHeight = self.getFieldHeight()

        # Coords for the top left corner of the boxes
        nameCoords = [self.getNameCoords()[0], self.getNameCoords()[1]]

        # Update the locations of the text boxes based on the heights
        newFieldY = self.getNameCoords()[1] + nameHeight
        newMethodY = self.getNameCoords()[1] + nameHeight + fieldHeight

        # Coordinates are based around the top left corner of the name box
        self.canvas.coords(self.getFieldObject(), self.getNameCoords()[0], newFieldY)
        self.canvas.coords(self.getMethodObject(), self.getNameCoords()[0], newMethodY)

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

    # --------------------------------------------------- #
    # Update coordinate list that can be called for relationship
    # --------------------------------------------------- #

    # This method populates widgetCoordinates list with lists of coordinate pairs
    # These are the coordinates for each of the four corners of the class widget,
    # Along with the center edge points between the corners
    def updateCoordinateList(self):
        # If the list has elements, delete all elements
        if self.widgetCoordinates:
            self.widgetCoordinates.clear()

        # Top middle [0]
        self.widgetCoordinates.append([((self.nameBoundingBox[0] + self.nameBoundingBox[2]) / 2), self.nameBoundingBox[1]])
        # Left middle [1]
        self.widgetCoordinates.append([self.nameBoundingBox[0], ((self.nameBoundingBox[1] + self.methodBoundingBox[3]) / 2)])
         # Right middle [2]
        self.widgetCoordinates.append([self.methodBoundingBox[2], ((self.nameBoundingBox[1] + self.methodBoundingBox[3]) / 2)])
        # Bottom middle [3]
        self.widgetCoordinates.append([((self.methodBoundingBox[0] + self.methodBoundingBox[2]) / 2), self.methodBoundingBox[3]])

        # Top left [4]
        self.widgetCoordinates.append([self.nameBoundingBox[0], self.nameBoundingBox[1]])
        # Top right [5]
        self.widgetCoordinates.append([self.nameBoundingBox[2], self.nameBoundingBox[1]])
        # Bottom left [6]
        self.widgetCoordinates.append([self.methodBoundingBox[0], self.methodBoundingBox[3]])
        # Bottom right [7]
        self.widgetCoordinates.append([self.methodBoundingBox[2], self.methodBoundingBox[3]])

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

    def moveBox(self, x, y):
        self.canvas.coords(self.getNameObject(), x, y)
        self.updateWidget()

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
    
    # Coordinates of text (top left)
    def getNameCoords(self):
        return self.canvas.coords(self.getNameObject())

    def getFieldCoords(self):
        return self.canvas.coords(self.getFieldObject())

    def getMethodCoords(self):
        return self.canvas.coords(self.getMethodObject())

    # Returns a list of two coordinateds for the top left corner of the widget. [x, y]
    def getWidgetCoords(self):
        return self.canvas.coords(self.getNameObject())

    # Width of each text
    def getNameWidth(self):
        nameBoundingBox = self.canvas.bbox(self.getNameObject())
        return nameBoundingBox[2] - nameBoundingBox[0]

    def getFieldWidth(self):
        fieldBoundingBox = self.canvas.bbox(self.getFieldObject())
        return fieldBoundingBox[2] - fieldBoundingBox[0]

    def getMethodWidth(self):
        methodBoundingBox = self.canvas.bbox(self.getMethodObject())
        return methodBoundingBox[2] - methodBoundingBox[0]

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
