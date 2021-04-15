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

        #(firstname, secondname): (x1, y1, x2, y2, type, destside, sourceside )
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

    
    def addClass(self, className, x, y):
        self.classDict[className] = ClassWidget(self, self.canvas, className, x, y)

    
    def deleteClass(self, className):
        self.classDict[className].deleteWidgetFromCanvas()
        del self.classDict[className]

        #updates the GUIs lineDictionary when classes are removed
        toDelete = []
        for theTuple in self.lineDict.keys():
            if className in theTuple:
                toDelete.append(theTuple)
                            
        for temp in toDelete:
            del self.lineDict[temp]
        self.drawLines()

    #updates the GUIs lineDictionary names
    def renameClass(self, oldName, newName):
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
                

    # Test popup box. Triggered in GUIMenuBar
    def boxTest(self):
        box = PopupBox("test")

    #erases all lines on the canvas (lines are stored in LineOBJlist), then redraws all lines from LineDict
    def drawLines(self):
        #usedSpaces = self.ClassSpaces()
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
                #randomPlacement  =

                #destSide           
                if(line[5] == 'bottom'):
                    side1 = (basepoint[0] + 5, basepoint[1] + 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] + 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] + 14)
                    localLineEnd = (basepoint[0] , basepoint[1] + 34)
                   # backTrackPoint =  (rootPoint[0], localLineEnd[1])
                if(line[5] == 'top'):
                    side1 = (basepoint[0] + 5, basepoint[1] - 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] - 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] - 14)
                    localLineEnd = (basepoint[0] , basepoint[1] - 34)
                    #backTrackPoint =  (rootPoint[0], localLineEnd[1])
                if(line[5] == 'left'):
                    side1 = (basepoint[0] - 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] - 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] - 14, basepoint[1])
                    localLineEnd = (basepoint[0] - 34, basepoint[1])
                    #backTrackPoint =  (localLineEnd[0], rootPoint[1])
                if(line[5] == 'right'):
                    side1 = (basepoint[0] + 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] + 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] + 14, basepoint[1])
                    localLineEnd = (basepoint[0] + 34, basepoint[1])
                    #backTrackPoint =  (localLineEnd[0], rootPoint[1])
                #src Side
                if(line[6] == 'bottom'):
                    rootEnd = (rootPoint[0], rootPoint[1] + 34)
                    backTrackPoint =  (rootEnd[0], localLineEnd[1])
                if(line[6] == 'top'):
                    rootEnd = (rootPoint[0], rootPoint[1] - 34)
                    backTrackPoint =  (rootEnd[0], localLineEnd[1])
                if(line[6] == 'left'):
                    rootEnd = (rootPoint[0] - 34, rootPoint[1])
                    backTrackPoint =  (localLineEnd[0], rootEnd[1])
                if(line[6] == 'right'):
                    rootEnd = (rootPoint[0] + 34, rootPoint[1])
                    backTrackPoint =  (localLineEnd[0], rootEnd[1])

                if(line[4] == 0 or line[4] == 1 ): #0 - aggregation & 1 - composition
                    if (line[4] == 0 ):
                        curfill = "white"
                    else:
                        curfill = "black"

                    #Source  Node
                    self.lineObjList.append(self.canvas.create_line(rootPoint[0], rootPoint[1], rootEnd[0], rootEnd[1]))
                    self.lineObjList.append(self.canvas.create_line(rootEnd[0], rootEnd[1], backTrackPoint[0], backTrackPoint[1]))

                    
                    self.lineObjList.append(self.canvas.create_line(backTrackPoint[0], backTrackPoint[1], localLineEnd[0], localLineEnd[1]))
                    
                    #Dest Node
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
    
    #adds a new line to the canvas
    def addLine(self, firstClassName, secondClassName, typ):
        #Find coordinates for shortest distance
        retVal = self.findShortestDistance(firstClassName, secondClassName)
        bothCoords = retVal[0]
        cord1 = bothCoords[0]
        cord2 = bothCoords[1]
        destSide = retVal[1]
        srcSide = retVal[2]
        typeList = ['aggregation', 'composition', 'inheritance', 'realization']
        if(type(typ) == int):
            numericTyp = typ
        else:
            numericTyp = typeList.index(typ)
        
        self.lineDict[(firstClassName, secondClassName)] = [cord1[0], cord1[1], cord2[0], cord2[1], numericTyp, destSide, srcSide]
        self.drawLines()
        self.canvas.update_idletasks

    #removes a line from the canvas
    def deleteLine(self, firstClassName, secondClassName):
        del self.lineDict[(firstClassName, secondClassName)]
        self.drawLines()

    #changes the type of a line on the canvas
    def renameLine(self, firstClassName, secondClassName, typ):
        del self.lineDict[(firstClassName, secondClassName)]
        self.drawLines()
        self.addLine(firstClassName, secondClassName, typ)
        self.drawLines()

    #finds the shortest distance between two classes
    def findShortestDistance(self, firstClassName, secondClassName):
        # Attain list of Snaps from the classes
        firstClassSnaps = self.classDict[firstClassName].widgetCoordinates
        secondClassSnaps = self.classDict[secondClassName].widgetCoordinates
        self.shortestDistance = 1000000
        firstClassCoord = 0
        secondClassCoord = 0
        
        destIteration = 0

        #iterate through all pairs of coordinates 
        srcIteration = 0
        for coord1 in firstClassSnaps:
            destIteration = 0
            for coord2 in secondClassSnaps: 
                 
                #calculate distance between points              
                XDis = coord1[0] - coord2[0]
                YDis = coord1[1] - coord2[1]
                self.currentDistance = abs(YDis) + abs(XDis)
                #check if any previous points were closer, it not. Replace it with the current distance
                if (round(self.currentDistance) + 3 < self.shortestDistance):
                    destSide = destIteration
                    srcSide = srcIteration
                    self.shortestDistance = self.currentDistance
                    firstClassCoord = coord1
                    secondClassCoord = coord2

                destIteration = destIteration + 1
            srcIteration = srcIteration + 1
        #return the closet points between the two classes
        return [(firstClassCoord, secondClassCoord), self.sideToString(destSide), self.sideToString(srcSide) ]

    def sideToString(self, sideNumber):
        leftList = [1, 4, 6]
        rightList = [2, 5, 7] 

        if(sideNumber in leftList):
            returnSide = 'left'
        elif(sideNumber in rightList):
            returnSide = 'right'
        elif(sideNumber == 0):
            returnSide = 'top'
        else:
            returnSide = 'bottom'   

        return returnSide

    def ClassSpaces(self):
        usedSpaces = []
        for className, classObj in self.lineDict.items():
            temp = self.classDict[className].widgetCoordinates
            usedSpaces.append(temp[4])
            usedSpaces.append(temp[7])
        return usedSpaces