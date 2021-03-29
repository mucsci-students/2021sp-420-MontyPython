from tkinter import *
from ClassWidget import ClassWidget
import math

# Inherits from frame class in tkinter
class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        
        # Master is root   
        self.master = master

        self.lineDict = {}

        #(firstname, secondname): (x1, y1, x2, y2, type, side )
        #Types: 0 - aggregation 1 - Composition 2 - inheritance 3- realization

        self.lineObjList = []
        #list of Canvas object Identifiers

        self.classDict = {}

        # Sets up window layout
        self.setup()      

    def setup(self):
        # Note: Menu bar is created within the controller
        # Set root's title
        self.master.title("UML Editor")

        # This widget will take up the full space of root

        #self.pack(fill=BOTH, expand=1)

        # Menu is set up in a different file to increase readability
        #self.menu = GUIMenuBar.menu(self, self.master) 

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

        # If it's not empty
        if self.lineObjList:
            #clear the list of canvas objects
            for i in self.lineObjList:
                self.canvas.delete(i)
        # If it's not empty
        if self.lineDict:
            #update the list of canvas objects using the lineDictionary
            #for key, value in d.items():
            for key, line in self.lineDict.items():
                if(line[4] == 0): #0 - aggregation               
                    if(line[5] == 'top'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3] - 10 ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] - 5 ,line[2], line[3] - 10 ,line[2] - 5, line[3] - 5,fill="white", outline = "black"))
                    if(line[5] == 'bottom'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3] + 10 ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] + 5 ,line[2], line[3] + 10 ,line[2] - 5, line[3] + 5,fill="white", outline = "black"))
                    if(line[5] == 'left'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2] - 10, line[3]))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] - 5 , line[3] - 5 ,line[2] - 10, line[3] ,line[2] - 5, line[3] + 5,fill="white", outline = "black"))
                    if(line[5] == 'right'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2] + 10, line[3] ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] - 5 ,line[2] + 10, line[3] ,line[2] + 5, line[3] + 5,fill="white", outline = "black"))
                if (line[4] == 1): #1 - Composition
                    if(line[5] == 'top'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3] - 10 ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] - 5 ,line[2], line[3] - 10 ,line[2] - 5, line[3] - 5, fill="black", outline = "black"))
                    if(line[5] == 'bottom'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3] + 10 ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] + 5 ,line[2], line[3] + 10 ,line[2] - 5, line[3] + 5, fill="black", outline = "black"))
                    if(line[5] == 'left'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2] - 10, line[3]))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] - 5 , line[3] - 5 ,line[2] - 10, line[3] ,line[2] - 5, line[3] + 5, fill="black", outline = "black"))
                    if(line[5] == 'right'):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2] + 10, line[3] ))
                        self.lineObjList.append(self.canvas.create_polygon(line[2], line[3], line[2] + 5 , line[3] - 5 ,line[2] + 10, line[3] ,line[2] + 5, line[3] + 5, fill="black"))
                if (line[4] == 2): #2 - inheritance
                    self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3], arrow=LAST))
                if(line[4] == 3): #3 - realization
                    self.lineObjList.append(self.canvas.create_line(line[0], line[1], line[2], line[3], dash=(5, 1), arrow=LAST))
    
    def addLine(self, firstClassName, secondClassName, typ):
        #Find coordinates for shortest distance
        retVal = self.findShortestDistance(firstClassName, secondClassName)
        bothCoords = retVal[0]
        cord1 = bothCoords[0]
        cord2 = bothCoords[1]
        side = retVal[1]
        typeList = ['aggregation', 'composition', 'inheritance', 'realization']
        self.lineDict[(firstClassName, secondClassName)] = [cord1[0], cord1[1], cord2[0], cord2[1], typeList.index(typ), side]
        self.drawLines()
        self.canvas.update_idletasks

    def deleteLine(self, firstClassName, secondClassName):
        del self.lineDict[(firstClassName, secondClassName)]
        self.drawLines()

    def renameLine(self, firstClassName, secondClassName, typ):
        del self.lineDict[(firstClassName, secondClassName)]
        self.drawLines()
        self.addLine(firstClassName, secondClassName, typ)
        self.drawLines()

    def findShortestDistance(self, firstClassName, secondClassName):
        # Attain list of Snaps from the classes
        firstClassSnaps = self.classDict[firstClassName].widgetCoordinates
        secondClassSnaps = self.classDict[secondClassName].widgetCoordinates
        self.shortestDistance = 1000000
        firstClassCoord = 0
        secondClassCoord = 0

        #iterate through all pairs of coordinates 
        for coord1 in firstClassSnaps:
            for coord2 in secondClassSnaps:  
                #calculate distance between points              
                XDis = coord1[0] - coord2[0]
                YDis = coord1[1] - coord2[1]
                self.currentDistance = abs(YDis) + abs(XDis)
                #check if any previous points were closer, it not. Replace it with the current distance
                if (round(self.currentDistance) < self.shortestDistance):
                    self.shortestDistance = self.currentDistance
                    firstClassCoord = coord1
                    secondClassCoord = coord2


        if(secondClassCoord[0] == self.classDict[secondClassName].x):
            return [(firstClassCoord, secondClassCoord), 'left']
        
        if(secondClassCoord[0] == self.classDict[secondClassName].methodBoundingBox[2]):
            return [(firstClassCoord, secondClassCoord), 'right']

        if(secondClassCoord[1] == self.classDict[secondClassName].y):
            return [(firstClassCoord, secondClassCoord), 'top']
    
        
        #return the closet points between the two classes
        return [(firstClassCoord, secondClassCoord), 'bottom']


