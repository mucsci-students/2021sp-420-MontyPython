from tkinter import *

#import GUI
# This needs to be modified, but it works
class AlertBox(object):
    pass

class AddClassBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(AddClassBox.root)

        frm = Frame(self.top, width=200, height=200, borderwidth=4, relief='ridge')
        frm.pack(fill="both", expand=True)
        frm.pack_propagate(0)

        lbl = Label(frm, text="Class Name")
        lbl.pack(padx=4, pady=4)

        name = Entry(frm)
        name.pack(padx=4, pady=4)

        btnCreate = Button(frm, text='Create')
        btnCreate['command'] =  lambda: controller.addClass(name.get())
        btnCreate.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)     
           
class DeleteClassBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(DeleteClassBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class RenameClassBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(RenameClassBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class AddFieldBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(AddFieldBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class RenameFieldBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(RenameFieldBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class DeleteFieldBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(DeleteFieldBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class AddMethodBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(AddMethodBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class DeleteMethodBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(DeleteMethodBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class RenameMethodBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(RenameMethodBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class AddParameterBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(AddParameterBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class DeleteParameterBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(DeleteParameterBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class ChangeParameterBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(ChangeParameterBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class AddRelationshipBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(AddRelationshipBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)

class DeleteRelationshipBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(DeleteRelationshipBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)
        
class ChangeRelationshipBox(object):
    root = None

    def __init__(self, msg, controller):

        self.top = Toplevel(ChangeRelationshipBox.root)

        frm = Frame(self.top, width=200, height=100, borderwidth=4, relief='ridge')
        frm.pack()
        frm.pack_propagate(0)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)
