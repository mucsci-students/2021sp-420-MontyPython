from tkinter import *
import GUIMenuBar
from ClassWidget import ClassWidget
from popuptest import PopupBox

# Inherits from frame class in tkinter
class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
           
        # Master is root   
        self.master = master
        # Sets up window layout
        self.setup()

        # TODO: delete when done testing
        self.testWidget = ClassWidget(self, self.canvas)

    def setup(self):

        # Set root's title
        self.master.title("UML Editor")

        # This widget will take up the full space of root
        self.pack(fill=BOTH, expand=1)

        # Menu is set up in a different file to increase readability
        self.menu = GUIMenuBar.menu(self, self.master) 

        # Create canvas for objects to be drawn on
        self.canvas = Canvas(self.master)

        # Both: Fills horizontally and vertically, expand: widget expands to fill extra space
        self.canvas.pack(fill="both", expand=True)

    # Test popup box. Triggered in GUIMenuBar
    def boxTest(self):
        box = PopupBox("test")

        


        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.