from tkinter import *

def menu(parent, root):     
    
    # Creates menu instance
    menu = Menu(parent, tearoff = False) 
    # Sets root's menu to this one 
    root.config(menu=menu)

    # Create file object
    file = Menu(menu, tearoff = False) 
    # Add option to file, set function to trigger
    file.add_command(label="Open") 
    file.add_command(label="Save")
    file.add_separator()
    file.add_command(label="Help")
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    # Adds file to menu bar
    menu.add_cascade(label="File", menu=file) 

    # Do the same for the rest of the menus
    classes = Menu(menu, tearoff = False)
    classes.add_command(label="Add Class", command=parent.boxTest)
    classes.add_command(label="Delete Class")
    classes.add_command(label="Rename Class")
    menu.add_cascade(label="Classes", menu=classes)

    fields = Menu(menu, tearoff = False)
    fields.add_command(label="Add Field")
    fields.add_command(label="Delete Field")
    fields.add_command(label="Rename Field")
    menu.add_cascade(label="Fields", menu=fields)

    methods = Menu(menu, tearoff = False)
    methods.add_command(label="Add Method")
    methods.add_command(label="Delete Method")
    methods.add_command(label="Rename Method")
    menu.add_cascade(label="Methods", menu=methods)
    methods.add_separator()
    methods.add_command(label="Add Parameter")
    methods.add_command(label="Delete Parameter")
    methods.add_command(label="Change Parameter")

    relationships = Menu(menu, tearoff = False)
    relationships.add_command(label="Add Relationship")
    relationships.add_command(label="Delete Relationship")
    relationships.add_command(label="Change Relationship")
    menu.add_cascade(label="Relationships", menu=relationships)