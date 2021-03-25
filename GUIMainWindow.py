from tkinter import *
from ClassWidget import ClassWidget

# Inherits from frame class in tkinter
class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   

        # Master is root   
        self.master = master

        self.classDict = {}

        # Sets up window layout
        self.setup()
        #self.lineDict = []          
        

    def setup(self):
        # Note: Menu bar is created within the controller
        # Set root's title
        self.master.title("UML Editor")

        # This widget will take up the full space of root
        # TODO: Figure out why this is causing problems, and if it's needed
        #self.pack(fill="both")

        # Create canvas for objects to be drawn on
        self.canvas = Canvas(self.master)

        # Both: Fills horizontally and vertically, expand: widget expands to fill extra space
        self.canvas.pack(fill=BOTH, expand=1)

    
    def addClass(self, className, x, y):
        # Note: Coordinates here are set to a default, but they should change
        self.classDict[className] = ClassWidget(self, self.canvas, className, x, y)

    # Test popup box. Triggered in GUIMenuBar
    def boxTest(self):
        box = PopupBox("test")

    #def drawLines

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
