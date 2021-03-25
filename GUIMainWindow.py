from tkinter import *
from ClassWidget import ClassWidget

# Inherits from frame class in tkinter
class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   

        # Master is root   
        self.master = master

        # Sets up window layout
        self.setup()      
  
        self.lineDict = []
        self.lineObjList = []
        self.classDict = {}
                       
        #(firstname, secondname): (x1, y1, x2, y2, type )
        #Types: 0 - aggregation 1 - Composition 2 - inheritance 3- realization

    def setup(self):
        # Note: Menu bar is created within the controller
        # Set root's title
        self.master.title("UML Editor")

        # This widget will take up the full space of root

        #self.pack(fill=BOTH, expand=1)

        # Menu is set up in a different file to increase readability
        self.menu = GUIMenuBar.menu(self, self.master) 

        # Create canvas for objects to be drawn on
        self.canvas = Canvas(self.master)
        
        # Both: Fills horizontally and vertically, expand: widget expands to fill extra space
        self.canvas.pack(fill=BOTH, expand=1)

        self.drawLines()
        #st = (200, 600)
        #nd = (100, 400)
       
        #point1 = ((nd[0] - st[0]) / 3 + st[0], (nd[1] - st[1]) / 3 + st[1])
        #point2  = ((((nd[0] - st[0]) / 3) * 1) + st[0] , (((nd[1] - st[1]) / 3) * 1)  + st[1])
        #point3
        #point4
        #self.canvas.create_line(st[0], st[1], point1[0], point1[1], )
        #self.canvas.create_line( point2[0], point2[1], nd[0], nd[1], )
        #self.canvas.create_line(300, 40, 300, 300, arrow=FIRST)


    
    def addClass(self, className, x, y):
        self.classDict[className] = ClassWidget(self, self.canvas, className, x, y)

    # Test popup box. Triggered in GUIMenuBar
    def boxTest(self):
        box = PopupBox("test")


    def drawLines(self):

        #clear the list of canvas objects
        for i in self.lineObjList:
            self.canvas.delete(i)
        
        #update the list of canvas objects using the lineDictionary
        for key, x in self.lineDict.items():
            if(x[4] == 0): #0 - aggregation 
                self.lineObjList.append(self.canvas.create_line(x[0], x[1], x[2], x[3], arrow=LAST))
            if (x[4] == 1): #1 - Composition
                self.lineObjList.append(self.canvas.create_line(x[0], x[1], x[2], x[3], arrow=LAST))
            if (x[4] == 2): #2 - inheritance
                 self.lineObjList.append(self.canvas.create_line(x[0], x[1], x[2], x[3], arrow=LAST))
            if(x[4] == 3): #3 - realization
                 self.lineObjList.append(self.canvas.create_line(x[0], x[1], x[2], x[3], dash=(5, 1), arrow=LAST))
    
    def addLine(self, firstClassName, secondClassName, x1, y1, x2, y2):
         self.lineDict[(firstClassName, secondClassName)] = [x1, y1, x2, y2]

    def deleteLine(self, firstClassName, secondClassName):
         del self.lineDict[(firstClassName, secondClassName)]

