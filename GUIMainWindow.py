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

        #(firstname, secondname): (x1, y1, x2, y2, type, destside, sourceside )
        #Types: 0 - aggregation 1 - Composition 2 - inheritance 3- realization

        self.lineObjList = []
        #list of Canvas object Identifiers

        self.classDict = {}

        # Sets up window layout
        self.setup()      

    def setup(self):
        self.master.title("UML Editor")

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
        height = self.master.winfo_height()
        width = self.master.winfo_width()
        # Expand the frame for the postscript file
        self.master.geometry("1920x1080")
        self.canvas.config(width=1920,height=1080)
        self.master.update()
        # Grab the postscript file
        ps = self.canvas.postscript(file="postscript.ps", colormode="color", pagewidth=1920, pageheight=1080, pagex=0, pagey=0)
        # Convert previous dimensions to a string
        dimensions = str(width)+"x"+str(height)
        # Restore the previous dimensions
        self.master.geometry(dimensions)
        self.canvas.config(width=width,height=height)
        self.canvas.update_idletasks
        self.master.update()

    
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
                self.deleteLine(oldName, name2, False)
                self.addLine(newName, name2, theType[4], False)
                
            else:
                self.deleteLine(name1, oldName, False)
                self.addLine(name1, newName, theType[4], False)
        self.drawLines()       

    def updateLineDict(self, className):
        # for theTuple in self.lineDict.keys():
        #     if className in theTuple:
        #         (name1, name2) = theTuple
        #         self.deleteLine(name1, name2)
        toUpdate = []
        typeList = []
        for theTuple, lineInfo in self.lineDict.items():
            if className in theTuple:
                toUpdate.append(theTuple)       
                typeList.append(lineInfo)     
                            
        for theTuple, theType in zip(toUpdate, typeList):
            (name1, name2) = theTuple
            self.deleteLine(name1, name2, False)
            self.addLine(name1, name2, theType[4], False)
        self.drawLines() 

    #erases all lines on the canvas (lines are stored in LineOBJlist), then redraws all lines from LineDict
    def drawLines(self):
        #print()
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
                    localLineEnd = (basepoint[0] , basepoint[1] + 16)
                   # backTrackPoint =  (rootPoint[0], localLineEnd[1])
                elif(line[5] == 'top'):
                    side1 = (basepoint[0] + 5, basepoint[1] - 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] - 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] - 14)
                    localLineEnd = (basepoint[0] , basepoint[1] - 16)
                    #backTrackPoint =  (rootPoint[0], localLineEnd[1])
                elif(line[5] == 'left'):
                    side1 = (basepoint[0] - 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] - 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] - 14, basepoint[1])
                    localLineEnd = (basepoint[0] - 16, basepoint[1])
                    #backTrackPoint =  (localLineEnd[0], rootPoint[1])
                elif(line[5] == 'right'):
                    side1 = (basepoint[0] + 7, basepoint[1] - 5 )
                    side2 = (basepoint[0] + 7, basepoint[1] + 5 )
                    furthestpoint = (basepoint[0] + 14, basepoint[1])
                    localLineEnd = (basepoint[0] + 16, basepoint[1])
                    #backTrackPoint =  (localLineEnd[0], rootPoint[1])
                #src Side
                if(line[6] == 'bottom'):
                    rootEnd = (rootPoint[0], rootPoint[1] + 5)
                elif(line[6] == 'top'):
                    rootEnd = (rootPoint[0], rootPoint[1] - 5)
                elif(line[6] == 'left'):
                    rootEnd = (rootPoint[0] - 5, rootPoint[1])
                elif(line[6] == 'right'):
                    rootEnd = (rootPoint[0] + 5, rootPoint[1])
                

                #Do Recursive Boi stuff here
                #Check if X or Y distance is greater
                xd = rootEnd[0] - localLineEnd[0] 
                yd = rootEnd[1] - localLineEnd[1]  

                if(abs(xd) > abs(yd)):
                    xf = localLineEnd[0] + (xd * .50)
                    backTrackPoint =  (xf, rootEnd[1])
                    backTrackPoint2 =  (xf, localLineEnd[1])
                else:
                    yf = localLineEnd[1] + (yd * .50)
                    backTrackPoint =  (rootEnd[0], yf)
                    backTrackPoint2 =  (localLineEnd[0], yf)

                if(basepoint == rootPoint):
                    basepoint = (line[2] + 5, line[3])
                    rootPoint = (line[0] - 5, line[1])
                    rootEnd = (rootPoint[0], rootPoint[1] - 20) 
                    side1 = (basepoint[0] + 5, basepoint[1] - 7 )
                    side2 = (basepoint[0] - 5, basepoint[1] - 7 )
                    furthestpoint = (basepoint[0] , basepoint[1] - 14)
                    localLineEnd = (basepoint[0] , basepoint[1] - 20)
                    backTrackPoint =  rootEnd
                    backTrackPoint2 =  rootEnd

                CoordinateList = [rootPoint[0], rootPoint[1], rootEnd[0], rootEnd[1], backTrackPoint[0], backTrackPoint[1], backTrackPoint2[0], backTrackPoint2[1], localLineEnd[0], localLineEnd[1], furthestpoint[0] , furthestpoint[1]]
                

                if(line[4] == 0 or line[4] == 1 ): #0 - aggregation & 1 - composition
                    if (line[4] == 0 ):
                        curfill = "white"
                    else:
                        curfill = "black"
                    self.lineObjList.append(self.canvas.create_line(CoordinateList))
                    self.lineObjList.append(self.canvas.create_polygon(side1[0], side1[1], basepoint[0], basepoint[1] ,side2[0], side2[1], furthestpoint[0], furthestpoint[1], fill=curfill, outline="black"))
                    #return
                if (line[4] == 2  or line[4] == 3): #2 - inheritance & 3 - realization
                    if (line[4] == 2 ):
                        self.lineObjList.append(self.canvas.create_line(CoordinateList, basepoint[0], basepoint[1],  arrow=LAST))
                    else:
                        self.lineObjList.append(self.canvas.create_line(CoordinateList, basepoint[0], basepoint[1], dash=(5,1), arrow=LAST))
                       
    
    #adds a new line to the canvas
    def addLine(self, firstClassName, secondClassName, typ, drawline):
        #Find coordinates for shortest distance
        typeList = ['aggregation', 'composition', 'inheritance', 'realization']
        if(type(typ) == int):
            numericTyp = typ
        else:
            numericTyp = typeList.index(typ)

        if(firstClassName == secondClassName): 
            temp = self.classDict[firstClassName].widgetCoordinates[0]
            self.lineDict[(firstClassName, secondClassName)] = [temp[0], temp[1], temp[0], temp[1], numericTyp, 0, 0]


        retVal = self.findShortestDistance(firstClassName, secondClassName)
        bothCoords = retVal[0]
        cord1 = bothCoords[0]
        cord2 = bothCoords[1]
        destSide = retVal[1]
        srcSide = retVal[2]
        
        
        self.lineDict[(firstClassName, secondClassName)] = [cord1[0], cord1[1], cord2[0], cord2[1], numericTyp, destSide, srcSide]
        if(drawline):
            self.drawLines()
            print(self.lineDict)
        self.canvas.update_idletasks

    #removes a line from the canvas
    def deleteLine(self, firstClassName, secondClassName, drawline):
        del self.lineDict[(firstClassName, secondClassName)]
        if(drawline):
            self.drawLines()

    #changes the type of a line on the canvas
    def renameLine(self, firstClassName, secondClassName, typ):
        del self.lineDict[(firstClassName, secondClassName)]
        self.drawLines()
        self.addLine(firstClassName, secondClassName, typ, True)
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
            s1 = self.sideToString(srcIteration)

            destIteration = 0
            for coord2 in secondClassSnaps: 
                #calculate distance between points                      
                s2 = self.sideToString(destIteration)       
               
                if(s1 == 'right'):
                    s1x = 24
                    s1y = 0
                elif(s1 == 'left'):
                    s1x = -24
                    s1y = 0
                elif(s1 == 'top'):
                    s1x = 0
                    s1y = -24
                else:
                    s1x = 0
                    s1y = 24
                 
                if(s2 == 'right'):
                    s2x = 24
                    s2y = 0
                elif(s2 == 'left'):
                    s2x = -24
                    s2y = 0
                elif(s2 == 'top'):
                    s2x = 0
                    s2y = -24
                else:
                    s2x = 0
                    s2y = 24
                self.currentDistance = math.dist([coord1[0] + s1x, coord1[1] + s1y],[coord2[0] + s2x, coord2[1] + s2y ])
                #self.currentDistance = abs(YDis) + abs(XDis)
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