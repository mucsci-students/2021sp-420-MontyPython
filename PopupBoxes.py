from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter import filedialog

class GenericBox:
    root = None
    
    def __init__(self, msg, errorMsg, controller):
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
    
    def addEntry(self, r, c, stick=W, px=4, py=4, ipx=50, txt=''):
        entry = Entry(self.frame)
        entry.grid(row=r, column=c, sticky=stick, padx=px, pady=py, ipadx=ipx)
        entry.configure(font=self.font, text=txt)
        return entry
    
    def addDropdown(self, r, c, entries, stick=W, px=4, py=4, ipx=40):
        cb = Combobox(self.frame, values=entries, state='readonly')
        cb.grid(row=r, column=c, sticky=stick, padx=px, pady=py, ipadx=ipx)
        cb.configure(font=self.font)
        return cb
    
    def splitMethodString(self, methodString):
        nameAndParams = methodString.split('(')
        name = nameAndParams[0].split(' ')[1]
        params = nameAndParams[1].split(', ')
        params[-1] = params[-1][:-1]
        if params[0] == '':
            params = []
        else:
            newParams = []
            for p in params:
                newParams.append(tuple(p.split()))
            params = newParams
        return name, params
    
    def clear(self, obj):
        obj.delete('0', 'end')

class AlertBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)
        errorString = f'Error: {errorMsg}'
        self.addLabel(errorString, 0, 0)
        self.frame.grab_set()
        
class SaveBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        filename = filedialog.asksaveasfilename(filetypes=[('Monty Python UML File', '*.monty')])
        controller.save(filename)       

class LoadBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        filename = filedialog.askopenfilename(filetypes=[('Monty Python UML File', '*.monty')])
        controller.load(filename)       

class HelpBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        lbl = self.addLabel('To interact with the UML diagram, use the menu at the top of the window.' +
                            '\nTo start, create a class.\nOnce a class is created, other elements can be added, ' +
                            'deleted, and modified.\nUp to nine classes can exist in the current form of this program.', 0, 0)
        lbl.configure(justify=LEFT)
        self.addButton('OK', 1, 1, S, self.top.destroy)

class AddClassBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)

        name = self.addEntry(0, 1)

        self.addButton('Create', 1, 0, W, lambda: controller.addClass(name.get()))
        self.addButton('Cancel', 1, 1, E, self.top.destroy)

class DeleteClassBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)

        name = self.addDropdown(0, 1, controller.getClasses())

        self.addButton('Delete', 1, 0, W, lambda: controller.deleteClass(name.get()))
        self.addButton('Cancel', 1, 1, E, self.top.destroy)

class RenameClassBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Old Class Name', 0, 0)
        self.addLabel('New Class Name', 1, 0)

        oldName = self.addDropdown(0, 1, controller.getClasses())
        newName = self.addEntry(1, 1)
        
        self.addButton('Rename', 2, 0, W,
                        lambda: controller.renameClass(oldName.get(), newName.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)

class AddFieldBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Field Type', 1, 0)
        self.addLabel('Field Name', 2, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        fieldType = self.addEntry(1, 1)
        fieldName = self.addEntry(2, 1)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.addField(className.get(), fieldName.get(), fieldType.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class DeleteFieldBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Field Name', 1, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.fieldName = self.addDropdown(1, 1, [])

        def dropdownEvent(event):
            if className.get() in controller.getClasses():
                self.fieldName.configure(values=controller.getFields(className.get()))
        
        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        self.addButton('Delete', 2, 0, W,
                       lambda: controller.deleteField(className.get(), self.fieldName.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)

class RenameFieldBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)
       
        self.addLabel('Class Name', 0, 0)
        self.addLabel('Old Field Name', 1, 0)
        self.addLabel('New Field Name', 2, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.oldName = self.addDropdown(1, 1, [])
        newName = self.addEntry(2, 1)

        def dropdownEvent(event):
            if className.get() in controller.getClasses():
                self.oldName.configure(values=controller.getFields(className.get()))
        
        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.renameField(className.get(), self.oldName.get(), newName.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class AddMethodBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        PARAM_LIMIT = 16

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Return Type', 1, 0)
        self.addLabel('Method Name', 2, 0)
        self.addLabel('Parameter Count', 4, 0)

        self.addLabel('Overloaded Methods', 3, 0)
        self.overloadLabel = self.addLabel('', 3, 1)

        className = self.addDropdown(0, 1, controller.getClasses())
        returnType = self.addEntry(1, 1)
        methodName = self.addEntry(2, 1)

        self.paramTypes = []
        self.paramNames = []
        self.paramLabel = self.addLabel('', 5, 0)
        self.paramCount = self.addEntry(4, 1, ipx=0)
        self.oldParamCount = ''

        # Function that triggers everytime a key is pressed
        def keyEvent(event):
            sv = StringVar()
            sv.set(controller.listMethods(className.get(), methodName.get(), numbered=False))
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

            # Get the parameter count as a string from the paramCount textbox
            pc = self.paramCount.get()
            psv = StringVar()
            if pc != '' and pc != self.oldParamCount:
                # Update the oldParamCount so things boxes update only when
                # they need to
                self.oldParamCount = pc

                # If need to update, yoink literally everything and put fresh boxes
                if len(self.paramTypes) > 0:
                    for t,n in zip(self.paramTypes, self.paramNames):
                        t.destroy()
                        n.destroy()
                self.paramTypes = []
                self.paramNames = []
                if int(pc) > PARAM_LIMIT:
                    psv.set('Parameter count too high')
                    self.paramLabel.configure(textvariable=psv, justify=LEFT)
                    return
                psv.set('Parameters (type followed by name)')
                self.paramLabel.configure(textvariable=psv, justify=LEFT)
                for r in range(6, 6+int(pc)):
                    self.paramTypes.append(self.addEntry(r, 0, ipx=50))
                    self.paramNames.append(self.addEntry(r, 1, ipx=50))
            elif pc != self.oldParamCount:
                self.oldParamCount = pc
                if len(self.paramTypes) > 0:
                    for t,n in zip(self.paramTypes, self.paramNames):
                        t.destroy()
                        n.destroy()
                self.paramTypes = []
                self.paramNames = []
                psv.set('')
                self.paramLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        def buttonEvent():
            params = []

            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if returnType.get() == '':
                errorString += "Please provide a return type\n"
                errorFlag = True
            
            if methodName.get() == '':
                errorString += "Please provide a method name\n"
                errorFlag = True       

            if self.paramCount.get() == '':
                errorString += "Please provide a parameter number"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            for t,n in zip(self.paramTypes, self.paramNames):
                params.append((t.get(), n.get()))
            
            controller.addMethod(className.get(), methodName.get(), returnType.get(), params)
            keyEvent(None)

        self.addButton('Add', 6+PARAM_LIMIT, 0, SW, buttonEvent)
        self.addButton('Cancel', 6+PARAM_LIMIT, 1, SE, self.top.destroy)


class DeleteMethodBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.methodName = self.addDropdown(1, 1, [])

        # Event bind function. Changes list of available methods based on what
        # class was selected.
        def dropdownEvent(event):
            if className.get() in controller.getClasses():
                vals = controller.getAllMethodsString(className.get())
                self.methodName.configure(values=vals)

        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        # self.addLabel('Method Number', 3, 0)
        # methodNum = self.addEntry(3, 1, ipx=0)

        def buttonEvent():

            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if self.methodName.get() == '':
                errorString += "Please provide a method name\n"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            name, params = self.splitMethodString(self.methodName.get())

            controller.deleteMethod(className.get(), name, params)
            self.clear(self.methodName)
            dropdownEvent(None)

        self.addButton('Delete', 4, 0, W, buttonEvent)
        self.addButton('Cancel', 4, 1, E, self.top.destroy)

class RenameMethodBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Old Method Name', 1, 0)
        self.addLabel('New Method Name', 2, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.methodName = self.addDropdown(1, 1, [])
        newMethodName = self.addEntry(2, 1)

        # Event bind function. Changes list of available methods based on what
        # class was selected.
        def dropdownEvent(event):
            if className.get() in controller.getClasses():
                vals = controller.getAllMethodsString(className.get())
                self.methodName.configure(values=vals)

        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        def buttonEvent():
            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if self.methodName.get() == '':
                errorString += "Please provide a method name\n"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            name, params = self.splitMethodString(self.methodName.get())
            controller.renameMethod(className.get(), name, params, newMethodName.get())
            self.clear(self.methodName)
            dropdownEvent(None)

        self.addButton('Rename', 5, 0, W, buttonEvent)
        self.addButton('Cancel', 5, 1, E, self.top.destroy)

class AddParameterBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)
        self.addLabel('Parameter Name', 2, 0)
        self.addLabel('Parameter Type', 3, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.methodName = self.addDropdown(1, 1, [])
        self.paramName = self.addEntry(2, 1)
        self.paramType = self.addEntry(3, 1)

        # Event bind function. Changes list of available methods based on what
        # class was selected.
        def dropdownEvent(event):
            if className.get() in controller.getClasses():
                vals = controller.getAllMethodsString(className.get())
                self.methodName.configure(values=vals)

        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        def buttonEvent():
            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if self.methodName.get() == '':
                errorString += "Please provide a method name\n"
                errorFlag = True

            if self.paramType.get() == '':
                errorString += "Please provide a parameter type\n"
                errorFlag = True
            
            if self.paramName.get() == '':
                errorString += "Please provide a parameter name\n"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            name, params = self.splitMethodString(self.methodName.get())
            controller.addParameter(className.get(), name, params, self.paramType.get(), self.paramName.get())
            self.clear(self.methodName)
            self.clear(self.paramType)
            self.clear(self.paramName)

            dropdownEvent(None)

        self.addButton('Add', 6, 0, W, buttonEvent)
        self.addButton('Cancel', 6, 1, E, self.top.destroy)


class DeleteParameterBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)
        self.addLabel('Parameter Name', 2, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.methodName = self.addDropdown(1, 1, [])
        self.paramName = self.addDropdown(2, 1, [])

        # Dropdown box event for methods, populates method dropdown with current
        # class selection
        def methodDropdownEvent(event):
            if className.get() in controller.getClasses():
                vals = controller.getAllMethodsString(className.get())
                self.methodName.configure(values=vals)
        
        # Populates parameter dropdown with params from current selected method
        def paramDropdownEvent(event):
            if (className.get() in controller.getClasses() 
                and self.methodName.get() in self.methodName['values']):
                _, vals = self.splitMethodString(self.methodName.get())
                self.paramName.configure(values=[p[1] for p in vals])

        # Calls both event functions
        def dropdownEvent(event):
            methodDropdownEvent(event)
            paramDropdownEvent(event)

        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        def buttonEvent():
            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if self.methodName.get() == '':
                errorString += "Please provide a method name"
                errorFlag = True

            if self.paramName.get() == '':
                errorString += "\nPlease provide a parameter name"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            # controller.removeParameter(className.get(), methodName.get(),
            # methodNum.get(), paramName.get())
            name, params = self.splitMethodString(self.methodName.get())
            controller.removeParameter(className.get(), name, params, self.paramName.get())
            self.clear(self.methodName)
            self.clear(self.paramName)

            keyEvent(None)

        self.addButton('Delete', 5, 0, W, buttonEvent)
        self.addButton('Cancel', 5, 1, E, self.top.destroy)

class ChangeParameterBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)
        self.addLabel('Old Parameter Name', 2, 0)
        self.addLabel('New Parameter Type', 3, 0)
        self.addLabel('New Parameter Name', 4, 0)

        className = self.addDropdown(0, 1, controller.getClasses())
        self.methodName = self.addDropdown(1, 1, [])
        self.oldParamName = self.addDropdown(2, 1, [])
        newParamType = self.addEntry(3, 1)
        newParamName = self.addEntry(4, 1)

        # Dropdown box event for methods, populates method dropdown with current
        # class selection
        def methodDropdownEvent(event):
            if className.get() in controller.getClasses():
                vals = controller.getAllMethodsString(className.get())
                self.methodName.configure(values=vals)
        
        # Populates parameter dropdown with params from current selected method
        def paramDropdownEvent(event):
            if (className.get() in controller.getClasses() 
                and self.methodName.get() in self.methodName['values']):
                _, vals = self.splitMethodString(self.methodName.get())
                self.oldParamName.configure(values=[p[1] for p in vals])

        # Calls both event functions
        def dropdownEvent(event):
            methodDropdownEvent(event)
            paramDropdownEvent(event)

        self.top.bind('<Key>', dropdownEvent)
        self.top.bind('<Button-1>', dropdownEvent)
        self.top.bind('<Motion>', dropdownEvent)

        def buttonEvent():
            errorFlag = False
            errorString = ''

            if className.get() == '':
                errorString += "\nPlease provide a class name\n"
                errorFlag = True
            
            if self.methodName.get() == '':
                errorString += "Please provide a method name"
                errorFlag = True

            if self.oldParamName.get() == '':
                errorString += "\nPlease provide the old parameter name"
                errorFlag = True

            if newParamType.get() == '':
                errorString += "\nPlease provide a new parameter type"
                errorFlag = True

            if newParamName.get() == '':
                errorString += "\nPlease provide the new parameter name"
                errorFlag = True

            if errorFlag:
                alertBox = controller.windowFactory("alertBox", errorString)
                return

            name, params = self.splitMethodString(self.methodName.get())
            controller.changeParameter(className.get(), name, params,
                                       self.oldParamName.get(), newParamType.get(), newParamName.get())

            self.clear(self.methodName)
            self.clear(self.oldParamName)

            dropdownEvent(None)

        self.addButton('Rename', 7, 0, W, buttonEvent)
        self.addButton('Cancel', 7, 1, E, self.top.destroy)

class AddRelationshipBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)
        self.addLabel('Relationship Type', 2, 0)

        sourceClass = self.addDropdown(0, 1, controller.getClasses())
        destClass = self.addDropdown(1, 1, controller.getClasses())

        types = ['aggregation', 'composition', 'inheritance', 'realization']
        relType = self.addDropdown(2, 1, types)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.addRelationship(sourceClass.get(), destClass.get(), relType.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)

class DeleteRelationshipBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)

        sourceClass = self.addDropdown(0, 1, controller.getClasses())
        destClass = self.addDropdown(1, 1, controller.getClasses())

        self.addButton('Delete', 2, 0, W,
                        lambda: controller.deleteRelationship(sourceClass.get(), destClass.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)
        
class ChangeRelationshipBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)
        self.addLabel('Relationship Type', 2, 0)

        sourceClass = self.addDropdown(0, 1, controller.getClasses())
        destClass = self.addDropdown(1, 1, controller.getClasses())

        types = ['aggregation', 'composition', 'inheritance', 'realization']
        relType = self.addDropdown(2, 1, types)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.renameRelationship(sourceClass.get(), destClass.get(), relType.get()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)
