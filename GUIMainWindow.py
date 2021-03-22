from tkinter import *
import GUIMenuBar
from ClassWidget import ClassWidget
from popuptest import AlertBox
from popuptest import AddClassBox
from popuptest import DeleteClassBox
from popuptest import *
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

    # Create a window using the factory method
    def windowFactory(self, windowType = "alertBox"):
    
        windows = {
            "alertBox": AlertBox,
            "Add Class": AddClassBox,
            "Delete Class": DeleteClassBox,
            "Rename Class": RenameClassBox,
            "Add Field": AddFieldBox,
            "Delete Field": DeleteFieldBox,
            "Rename Field": RenameFieldBox,
            "Add Method": AddMethodBox,
            "Delete Method": DeleteMethodBox,
            "Rename Method": RenameMethodBox,
            "Add Parameter": AddParameterBox,
            "Delete Parameter": DeleteParameterBox,
            "Change Parameter": ChangeParameterBox,
            "Add Relationship": AddRelationshipBox,
            "Delete Relationship": DeleteRelationshipBox,
            "Change Relationship": ChangeRelationshipBox
        }
        
        # Show window
        box = windows[windowType](windowType)

        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.