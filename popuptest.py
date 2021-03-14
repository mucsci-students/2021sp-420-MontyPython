from tkinter import *

# This needs to be modified, but it works
class PopupBox(object):

    root = None

    def __init__(self, msg):

        self.top = Toplevel(PopupBox.root)

        frm = Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        lbl = Label(frm, text=msg)
        lbl.pack(padx=4, pady=4)

        btnCancel = Button(frm, text='Cancel')
        btnCancel['command'] = self.top.destroy
        btnCancel.pack(padx=4, pady=4)
