from tkinter import *

def menu(controller, view, root):     
    
    # Creates menu instance
    menu = Menu(view, tearoff = False) 
    # Sets root's menu to this one 
    root.config(menu=menu)

    # Create file object
    file = Menu(menu, tearoff = False) 
    # Add option to file, set function to trigger
    file.add_command(label="Open", command= lambda: controller.windowFactory("Open")) 
    file.add_command(label="Save", command= lambda: controller.windowFactory("Save"))
    file.add_separator()
    file.add_command(label="Help", command=lambda: controller.windowFactory("Help"))
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    # Adds file to menu bar
    menu.add_cascade(label="File", menu=file) 

    # Do the same for the rest of the menus
    classes = Menu(menu, tearoff = False)
    classes.add_command(label="Add Class", command= lambda: controller.windowFactory("Add Class"))
    classes.add_command(label="Delete Class", command= lambda: controller.windowFactory("Delete Class"))
    classes.add_command(label="Rename Class", command= lambda: controller.windowFactory("Rename Class"))
    menu.add_cascade(label="Classes", menu=classes)

    fields = Menu(menu, tearoff = False)
    fields.add_command(label="Add Field", command= lambda: controller.windowFactory("Add Field"))
    fields.add_command(label="Delete Field", command= lambda: controller.windowFactory("Delete Field"))
    fields.add_command(label="Rename Field", command= lambda: controller.windowFactory("Rename Field"))
    menu.add_cascade(label="Fields", menu=fields)

    methods = Menu(menu, tearoff = False)
    methods.add_command(label="Add Method", command= lambda: controller.windowFactory("Add Method"))
    methods.add_command(label="Delete Method", command= lambda: controller.windowFactory("Delete Method"))
    methods.add_command(label="Rename Method", command= lambda: controller.windowFactory("Rename Method"))
    menu.add_cascade(label="Methods", menu=methods)
    methods.add_separator()
    methods.add_command(label="Add Parameter", command= lambda: controller.windowFactory("Add Parameter"))
    methods.add_command(label="Delete Parameter", command= lambda: controller.windowFactory("Delete Parameter"))
    methods.add_command(label="Change Parameter", command= lambda: controller.windowFactory("Change Parameter"))

    relationships = Menu(menu, tearoff = False)
    relationships.add_command(label="Add Relationship", command= lambda: controller.windowFactory("Add Relationship"))
    relationships.add_command(label="Delete Relationship", command= lambda: controller.windowFactory("Delete Relationship"))
    relationships.add_command(label="Change Relationship", command= lambda: controller.windowFactory("Change Relationship"))
    menu.add_cascade(label="Relationships", menu=relationships)