from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox

class GenericBox:
    root = None
    
    def __init__(self, msg, controller):
        self.top = Toplevel(GenericBox.root)
        self.top.resizable(False, False)
        self.top.title(msg)

        self.frame = Frame(self.top, borderwidth=4, relief='ridge')
        self.frame.pack(fill='both', expand=True)

        f = Font(name='TkDefaultFont', exists=True).actual()['family']
        self.font = Font(family=f, size=12)

    # Parameters for add functions:
    # r - row in grid
    # c - column in grid
    # stick - edge/corner element will stick to
    # txt - text shown
    # px - padding x
    # py - padding y
    # ipx - internal padding, i.e. width

    def addButton(self, txt, r, c, stick, cmd, px=4, py=4, ipx=20):
        btn = Button(self.frame, text=txt)
        btn['command'] = cmd
        btn.grid(row=r, column=c, sticky=stick, padx=px, pady=py, ipadx=20)
        btn.configure(font=self.font)
        return btn
    
    def addLabel(self, txt, r, c, stick=W, px=4, py=4):
        lbl = Label(self.frame, text=txt)
        lbl.grid(row=r, column=c, sticky=stick, padx=px, pady=py)
        lbl.configure(font=self.font)
        return lbl
    
    def addEntry(self, r, c, stick=W, px=4, py=4, ipx=50):
        entry = Entry(self.frame)
        entry.grid(row=r, column=c, sticky=stick, padx=px, pady=py, ipadx=ipx)
        entry.configure(font=self.font)
        return entry

# This needs to be modified, but it works
class AlertBox(GenericBox):
    pass

class AddClassBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Class Name', 0, 0)

        name = self.addEntry(0, 1)

        self.addButton('Create', 1, 0, W, lambda: controller.addClass(name.get()))
        self.addButton('Cancel', 1, 1, E, self.top.destroy)

class DeleteClassBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Class Name', 0, 0)

        name = self.addEntry(0, 1)

        self.addButton('Delete', 1, 0, W, lambda: controller.deleteClass(name.get()))
        self.addButton('Cancel', 1, 1, E, self.top.destroy)

class RenameClassBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Old Class Name', 0, 0)
        self.addLabel('New Class Name', 1, 0)

        oldName = self.addEntry(0, 1)
        newName = self.addEntry(1, 1)
        
        self.addButton('Rename', 2, 0, W,
                        lambda: controller.renameClass(oldName.get(), newName.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)

class AddFieldBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Field Type', 1, 0)
        self.addLabel('Field Name', 2, 0)

        className = self.addEntry(0, 1)
        fieldType = self.addEntry(1, 1)
        fieldName = self.addEntry(2, 1)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.addField(className.get(), fieldName.get(), typeName.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class DeleteFieldBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Field Name', 1, 0)

        className = self.addEntry(0, 1)
        fieldName = self.addEntry(1, 1)

        self.addButton('Delete', 2, 0, W,
                       lambda: controller.deleteField(className.get(), fieldName.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)

class RenameFieldBox(GenericBox):
    root = None

    def __init__(self, msg, controller):
        super().__init__(msg, controller)
       
        self.addLabel('Class Name', 0, 0)
        self.addLabel('Old Field Name', 1, 0)
        self.addLabel('New Field Name', 2, 0)

        className = self.addEntry(0, 1)
        oldName = self.addEntry(1, 1)
        newName = self.addEntry(2, 1)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.renameField(className.get(), oldName.get(), newName.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class AddMethodBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class DeleteMethodBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class RenameMethodBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class AddParameterBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class DeleteParameterBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class ChangeParameterBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

class AddRelationshipBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)
        self.addLabel('Relationship Type', 2, 0)

        sourceClass = self.addEntry(0, 1)
        destClass = self.addEntry(1, 1)

        types = ['aggregation', 'composition', 'inheritance', 'realization']
        relType = Combobox(self.frame, values=types)
        relType.grid(row=2, column=1, sticky=W, padx=4, pady=4)
        relType.configure(font=self.font)

        self.addButton('Create', 3, 0, W,
                lambda: controller.addRelationship(sourceClass.get(), destClass.get(), relType.current()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class DeleteRelationshipBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)
        
class ChangeRelationshipBox(GenericBox):
    def __init__(self, msg, controller):
        super().__init__(msg, controller)
