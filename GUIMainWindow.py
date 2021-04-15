from tkinter import *
from ClassWidget import ClassWidget
import math
from PIL import Image
import time

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

    # grab all the changes made to the canvas and update the postscript file. used for
    # export as image.
    def updatePsFile(self):
        
        self.master.update()
        # Store the width and height of the frame
        height = self.master.winfo_screenheight()
        width = self.master.winfo_screenwidth()
        # Expand the frame for the postscript file
        self.master.geometry("2000x1800")
        self.canvas.config(width=2000,height=1800)
        self.master.update()
        # Grab the postscript file
        ps = self.canvas.postscript(file="postscript.ps", colormode="color", pagewidth=5000, pageheight=4000, pagex=0, pagey=0)
        # Convert previous dimensions to a string
        dimensions = str(width)+"x"+str(height)
        print(dimensions)
        # Restore the previous dimensions
        self.master.geometry(dimensions)
        self.canvas.config(width=width,height=height)
        self.canvas.update_idletasks
        self.master.update()

    def addClass(self, className, x, y):
        self.classDict[className] = ClassWidget(self, self.canvas, className, x, y)
        # Binds are for move class
        self.canvas.tag_bind(className, '<ButtonPress-1>', lambda e, tag=className: self.startDrag(e, tag))
        self.canvas.tag_bind(className, '<B1-Motion>', lambda e, tag=className: self.dragMotion(e, tag))

    # Starts move class drag
    def startDrag(self, event, tag):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    # Moves class with left click
    def dragMotion(self, event, tag):
        widget = event.widget
        x = event.x - widget.startX
        y = event.y - widget.startY

        self.canvas.move(tag, x, y)
        widget.startX = event.x
        widget.startY = event.y

    def deleteClass(self, className):
        self.classDict[className].deleteWidgetFromCanvas()
        del self.classDict[className]

        toDelete = []
        for theTuple in self.lineDict.keys():
            if className in theTuple:
                toDelete.append(theTuple)
                            
        for temp in toDelete:
            del self.lineDict[temp]
        self.drawLines()

    def renameClass(self, oldName, newName):
        print("LIne Dictionary")
        print(self.lineDict)
        print(self.classDict)
        toChange = []
        typeList = []
        for theTuple, lineInfo in self.lineDict.items():
            if oldName in theTuple:
                toChange.append(theTuple)       
                typeList.append(lineInfo)     
                            
        for theTuple, theType in zip(toChange, typeList):
            (name1, name2) = theTuple
            if name1 == oldName:
                self.deleteLine(oldName, name2)
                self.addLine(newName, name2, theType[4])
                
            else:
                self.deleteLine(name1, oldName)
                self.addLine(name1, newName, theType[4])
                
        #self.drawLines()
        #print("LIne Dictionary")
        #print(self.lineDict)
        #self.drawLines()

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
                basepoint = (line[2], line[3])
                rootPoint = (line[0], line[1])              
                if(line[5] == 'bottom'):
                    side1 = (basepoint[0] + 5, basepoint[1] + 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] + 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] + 14)
                    localLineEnd = (basepoint[0] , basepoint[1] + 34)
                    backTrackPoint =  (rootPoint[0], localLineEnd[1])
                if(line[5] == 'top'):
                    side1 = (basepoint[0] + 5, basepoint[1] - 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] - 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] - 14)
                    localLineEnd = (basepoint[0] , basepoint[1] - 34)
                    backTrackPoint =  (rootPoint[0], localLineEnd[1])
                if(line[5] == 'left'):
                    side1 = (basepoint[0] - 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] - 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] - 14, basepoint[1])
                    localLineEnd = (basepoint[0] - 34, basepoint[1])
                    backTrackPoint =  (localLineEnd[0], rootPoint[1])
                if(line[5] == 'right'):
                    side1 = (basepoint[0] + 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] + 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] + 14, basepoint[1])
                    localLineEnd = (basepoint[0] + 34, basepoint[1])
                    backTrackPoint =  (localLineEnd[0], rootPoint[1])
                if(line[4] == 0 or line[4] == 1 ): #0 - aggregation & 1 - composition
                    if (line[4] == 0 ):
                        curfill = "white"
                    else:
                        curfill = "black"
                    self.lineObjList.append(self.canvas.create_line(line[0], line[1], backTrackPoint[0], backTrackPoint[1]))
                    self.lineObjList.append(self.canvas.create_line(backTrackPoint[0], backTrackPoint[1], localLineEnd[0], localLineEnd[1]))
                    self.lineObjList.append(self.canvas.create_line(furthestpoint[0] , furthestpoint[1], localLineEnd[0], localLineEnd[1]))
                    self.lineObjList.append(self.canvas.create_polygon(basepoint[0], basepoint[1], side1[0], side1[1] , furthestpoint[0] , furthestpoint[1],side2[0], side2[1],fill=curfill, outline = "black"))
    
                if (line[4] == 2  or line[4] == 3): #2 - inheritance & 3 - realization
                    if (line[4] == 2 ):
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], backTrackPoint[0], backTrackPoint[1]))
                        self.lineObjList.append(self.canvas.create_line(backTrackPoint[0], backTrackPoint[1], localLineEnd[0], localLineEnd[1]))
                        self.lineObjList.append(self.canvas.create_line(localLineEnd[0], localLineEnd[1], basepoint[0], basepoint[1], arrow=LAST))               
                    else:
                        self.lineObjList.append(self.canvas.create_line(line[0], line[1], backTrackPoint[0], backTrackPoint[1], dash=(5,1)))
                        self.lineObjList.append(self.canvas.create_line(backTrackPoint[0], backTrackPoint[1], localLineEnd[0], localLineEnd[1], dash=(5,1)))
                        self.lineObjList.append(self.canvas.create_line(localLineEnd[0], localLineEnd[1], basepoint[0], basepoint[1], dash=(5,1), arrow=LAST))
                
    def addLine(self, firstClassName, secondClassName, typ):
        #Find coordinates for shortest distancec
        retVal = self.findShortestDistance(firstClassName, secondClassName)
        bothCoords = retVal[0]
        cord1 = bothCoords[0]
        cord2 = bothCoords[1]
        side = retVal[1]
        typeList = ['aggregation', 'composition', 'inheritance', 'realization']
        if(type(typ) == int):
            numericTyp = typ
        else:
            numericTyp = typeList.index(typ)
        
        self.lineDict[(firstClassName, secondClassName)] = [cord1[0], cord1[1], cord2[0], cord2[1], numericTyp, side]
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
        secondIteration = 0

        #iterate through all pairs of coordinates 
        for coord1 in firstClassSnaps:
            secondIteration = 0
            for coord2 in secondClassSnaps: 
                 
                #calculate distance between points              
                XDis = coord1[0] - coord2[0]
                YDis = coord1[1] - coord2[1]
                self.currentDistance = abs(YDis) + abs(XDis)
                #check if any previous points were closer, it not. Replace it with the current distance
                if (round(self.currentDistance) + 7 < self.shortestDistance):
                    iterationSide = secondIteration
                    self.shortestDistance = self.currentDistance
                    firstClassCoord = coord1
                    secondClassCoord = coord2
                secondIteration = secondIteration + 1

        print(iterationSide)
        if(iterationSide == 1 or iterationSide == 4 or iterationSide == 6):
            return [(firstClassCoord, secondClassCoord), 'left']
        
        if(iterationSide == 2 or iterationSide == 5 or iterationSide == 7):
            return [(firstClassCoord, secondClassCoord), 'right']

        if(iterationSide == 0):
            
            return [(firstClassCoord, secondClassCoord), 'top']
        
        #return the closet points between the two classes
        return [(firstClassCoord, secondClassCoord), 'bottom']

