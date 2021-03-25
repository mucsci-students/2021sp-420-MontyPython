from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox

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

class AlertBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)
        errorString = f'Error: {errorMsg}'
        self.addLabel(errorString, 0, 0)
        self.frame.grab_set()
        


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

        name = self.addEntry(0, 1)

        self.addButton('Delete', 1, 0, W, lambda: controller.deleteClass(name.get()))
        self.addButton('Cancel', 1, 1, E, self.top.destroy)

class RenameClassBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Old Class Name', 0, 0)
        self.addLabel('New Class Name', 1, 0)

        oldName = self.addEntry(0, 1)
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

        className = self.addEntry(0, 1)
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

        className = self.addEntry(0, 1)
        fieldName = self.addEntry(1, 1)

        self.addButton('Delete', 2, 0, W,
                       lambda: controller.deleteField(className.get(), fieldName.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)

class RenameFieldBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)
       
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
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        PARAM_LIMIT = 10

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Return Type', 1, 0)
        self.addLabel('Method Name', 2, 0)
        self.addLabel('Parameter Count', 4, 0)

        self.addLabel('Overloaded Methods', 3, 0)
        self.overloadLabel = self.addLabel('', 3, 1)

        className = self.addEntry(0, 1)
        returnType = self.addEntry(1, 1)
        methodName = self.addEntry(2, 1)

        self.paramTypes = []
        self.paramNames = []
        self.paramLabel = self.addLabel('', 5, 0)
        self.paramCount = self.addEntry(4, 1, ipx=0)
        self.oldParamCount = ''

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add duplicate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                sv.set('\n'.join(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()])))
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
            for t,n in zip(self.paramTypes, self.paramNames):
                params.append([t.get(), n.get()])
            controller.addMethod(className.get(), methodName.get(), returnType.get(), params)
            keyEvent(None)

        self.addButton('Add', 6+PARAM_LIMIT, 0, SW, buttonEvent)
        self.addButton('Cancel', 6+PARAM_LIMIT, 1, SE, self.top.destroy)


class DeleteMethodBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)

        self.addLabel('Overloaded Methods', 2, 0)
        self.overloadLabel = self.addLabel('', 2, 1)

        className = self.addEntry(0, 1)
        methodName = self.addEntry(1, 1)

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add dupl icate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                methods = list(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()]))
                s = ''
                for i in range(len(methods)):
                    s += f'{i+1}. {methods[i]}\n'
                sv.set(s.strip())
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        self.addLabel('Method Number', 3, 0)
        methodNum = self.addEntry(3, 1, ipx=0)

        def buttonEvent():
            controller.deleteMethod(className.get(), methodName.get(), 
                       controller.model.classDict[className.get()].methodDict[methodName.get()][int(methodNum.get())-1].parameters)
            keyEvent(None)

        self.addButton('Delete', 4, 0, W, buttonEvent)
        self.addButton('Cancel', 4, 1, E, self.top.destroy)

class RenameMethodBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Old Method Name', 1, 0)
        self.addLabel('New Method Name', 2, 0)

        self.addLabel('Overloaded Methods', 3, 0)
        self.overloadLabel = self.addLabel('', 3, 1)

        className = self.addEntry(0, 1)
        methodName = self.addEntry(1, 1)
        newMethodName = self.addEntry(2, 1)

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add dupl icate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                methods = list(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()]))
                s = ''
                for i in range(len(methods)):
                    s += f'{i+1}. {methods[i]}\n'
                sv.set(s.strip())
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        self.addLabel('Method Number', 4, 0)
        methodNum = self.addEntry(4, 1, ipx=0)

        def buttonEvent():
            controller.renameMethod(className.get(), methodName.get(), 
                       controller.model.classDict[className.get()].methodDict[methodName.get()][int(methodNum.get())-1].parameters,
                       newMethodName.get())
            keyEvent(None)

        self.addButton('Rename', 5, 0, W, buttonEvent)
        self.addButton('Cancel', 5, 1, E, self.top.destroy)

class AddParameterBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)
        self.addLabel('Parameter Name', 2, 0)
        self.addLabel('Parameter Type', 3, 0)

        self.addLabel('Overloaded Methods', 4, 0)
        self.overloadLabel = self.addLabel('', 4, 1)

        className = self.addEntry(0, 1)
        methodName = self.addEntry(1, 1)
        paramType = self.addEntry(2, 1)
        paramName = self.addEntry(3, 1)

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add dupl icate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                methods = list(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()]))
                s = ''
                for i in range(len(methods)):
                    s += f'{i+1}. {methods[i]}\n'
                sv.set(s.strip())
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        self.addLabel('Method Number', 5, 0)
        methodNum = self.addEntry(5, 1, ipx=0)

        def buttonEvent():
            controller.addParameter(className.get(), methodName.get(), 
                       controller.model.classDict[className.get()].methodDict[methodName.get()][int(methodNum.get())-1].parameters, paramType.get(), paramName.get())
            keyEvent(None)

        self.addButton('Add', 6, 0, W, buttonEvent)
        self.addButton('Cancel', 6, 1, E, self.top.destroy)


class DeleteParameterBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Class Name', 0, 0)
        self.addLabel('Method Name', 1, 0)
        self.addLabel('Parameter Name', 2, 0)

        self.addLabel('Overloaded Methods', 3, 0)
        self.overloadLabel = self.addLabel('', 3, 1)

        className = self.addEntry(0, 1)
        methodName = self.addEntry(1, 1)
        paramName = self.addEntry(2, 1)

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add dupl icate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                methods = list(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()]))
                s = ''
                for i in range(len(methods)):
                    s += f'{i+1}. {methods[i]}\n'
                sv.set(s.strip())
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        self.addLabel('Method Number', 4, 0)
        methodNum = self.addEntry(4, 1, ipx=0)

        def buttonEvent():
            controller.removeParameter(className.get(), methodName.get(), 
                       controller.model.classDict[className.get()].methodDict[methodName.get()][int(methodNum.get())-1].parameters, paramName.get())
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

        self.addLabel('Overloaded Methods', 5, 0)
        self.overloadLabel = self.addLabel('', 5, 1)

        className = self.addEntry(0, 1)
        methodName = self.addEntry(1, 1)
        oldParamName = self.addEntry(2, 1)
        newParamType = self.addEntry(3, 1)
        newParamName = self.addEntry(4, 1)

        # Yes I am defining a function within a function otherwise the lambda in
        # the self.top.bind call is horrendous
        # 
        # This function essentially updates the Overloaded Methods label based
        # on what is in the methodName textbox. If a method that is in there
        # happens to exist, it will list every instance of the method within
        # that class, that way the user knows not to add dupl icate methods.
        def keyEvent(event):
            sv = StringVar()
            if (className.get() in controller.model.classDict and 
                methodName.get() in controller.model.classDict[className.get()].methodDict):
                methods = list(map(str, controller.model.classDict[className.get()].methodDict[methodName.get()]))
                s = ''
                for i in range(len(methods)):
                    s += f'{i+1}. {methods[i]}\n'
                sv.set(s.strip())
            self.overloadLabel.configure(textvariable=sv, justify=LEFT)

        self.top.bind('<Key>', lambda e: keyEvent(e))

        self.addLabel('Method Number', 6, 0)
        methodNum = self.addEntry(6, 1, ipx=0)

        def buttonEvent():
            controller.changeParameter(className.get(), methodName.get(), 
                       controller.model.classDict[className.get()].methodDict[methodName.get()][int(methodNum.get())-1].parameters, oldParamName.get(), newParamName.get(), newParamName.get())
            keyEvent(None)

        self.addButton('Rename', 7, 0, W, buttonEvent)
        self.addButton('Cancel', 7, 1, E, self.top.destroy)

class AddRelationshipBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

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
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)

        sourceClass = self.addEntry(0, 1)
        destClass = self.addEntry(1, 1)

        self.addButton('Delete', 2, 0, W,
                        lambda: controller.deleteRelationship(sourceClass.get(), destClass.get()))
        self.addButton('Cancel', 2, 1, E, self.top.destroy)
        
class ChangeRelationshipBox(GenericBox):
    def __init__(self, msg, errorMsg, controller):
        super().__init__(msg, errorMsg, controller)

        self.addLabel('Source Class', 0, 0)
        self.addLabel('Destination Class', 1, 0)

        sourceClass = self.addEntry(0, 1)
        destClass = self.addEntry(1, 1)

        types = ['aggregation', 'composition', 'inheritance', 'realization']
        relType = Combobox(self.frame, values=types)
        relType.grid(row=2, column=1, sticky=W, padx=4, pady=4)
        relType.configure(font=self.font)

        self.addButton('Create', 3, 0, W,
                        lambda: controller.changeRelationship(sourceClass.get(), destClass.get(), relType.current()))
        self.addButton('Cancel', 3, 1, E, self.top.destroy)
