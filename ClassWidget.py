from tkinter import *

class ClassWidget(Frame):
    def __init__(self, parent, canvas):
        Frame.__init__(self, parent)

        self.canvas = canvas
        # Contains objects NameText, NameBox, FieldText, FieldBox, MethodText, MethodBox
        self.objectDict = {}

        #TODO: Create textbox for name, make the other two with "" for the text
        #TODO: If anything is updated, boxes will have to be redrawn

        self.createTextBox(200, 200, "Name", "Name")
        self.createTextBox(200, 300, "Field", "")
        self.createTextBox(200, 400, "Method", "")

        

        # Gets coordiantes of the name text box to use in other methods
        # [x1, y1, x2, y2]
        self.nameLoc = self.canvas.bbox(self.objectDict["NameText"])
        # Set widths of all boxes to match the largest one
        self.setWidths()

        # TODO: Unfinished
        for obj in self.objectDict:
            canvas.tag_bind(obj, '<Button1-Motion>', self.move)
            canvas.tag_bind(obj, '<ButtonRelease-1>', self.release)
        self.clicked = False

    # TODO: unfinished, still figuring this out
    def move(self, event):
        if self.clicked:       
            self.canvas.move(obj, event.x - self.mouseX, event.y - self.mouseY)
            self.mouseX = event.x
            self.mouseY = event.y
        else:
            self.clicked = True
            self.canvas.tag_raise(obj)
            self.mouseX = event.x
            self.mouseY = event.y
 
    def release(self, event):
        self.clicked = False
        

    # Finds the box with the largest width and sets all boxes to that width\
    # TODO: Stopped here, width isn't workign properly
    def setWidths(self):
        # Get widths
        fieldWidth = self.canvas.bbox(self.objectDict["FieldText"])
        methodWidth = self.canvas.bbox(self.objectDict["MethodText"])
        nameWidth = self.nameLoc[2] - self.nameLoc[0]
        fieldWidth = fieldWidth[2] - fieldWidth[0]
        methodWidth = methodWidth[2] - methodWidth[0]

        # Find largest
        if methodWidth > fieldWidth and methodWidth > nameWidth:
            w = methodWidth
        elif fieldWidth > methodWidth and fieldWidth > nameWidth:
            w = fieldWidth
        elif nameWidth > fieldWidth and nameWidth > methodWidth:
            w = nameWidth

        # Update text boxes with the new widths
        self.canvas.itemconfig(self.objectDict["NameText"], width=w)
        self.canvas.itemconfig(self.objectDict["FieldText"], width=w)
        self.canvas.itemconfig(self.objectDict["MethodText"], width=w)
        self.canvas.update()
        self.drawBox(w, "Name", self.objectDict["NameText"])
        self.drawBox(w, "Field", self.objectDict["FieldText"])
        self.drawBox(w, "Method", self.objectDict["MethodText"])
    
    # Creates box that goes around text. 
    # Identifier = Name, Field, or Method
    # txtBox = objectDict entry
    # w = width
    def drawBox(self, w, identifier, txtBox):
        # bbox returns a list [x1, y1, x2, y2]
        boundingBox = self.canvas.bbox(txtBox)
        # Create the actual box
        # create_rectangle: x1, y1, x2, y2, options..
        # (x1, y1) top left corner, (x2, y2) bottom right corner
        self.objectDict[identifier + "Box"] = self.canvas.create_rectangle(boundingBox[0], boundingBox[1], (boundingBox[0] + w), boundingBox[3], outline="black", fill="white")
        # Moves items up to be in front of other objects
        self.canvas.tag_raise(self.objectDict[identifier + "Box"])
        self.canvas.tag_raise(self.objectDict[identifier + "Text"])

    # Creates the text for the text box. 
    # x, y = coordinates
    # Identifier = Name, Field, or Method 
    # Txt = the text to go inside the box
    def createTextBox(self, x, y, identifier, txt):
        # create_text(x, y, options ...)
        self.objectDict[identifier + "Text"] = self.canvas.create_text(x, y, text = txt, fill="black")
        

