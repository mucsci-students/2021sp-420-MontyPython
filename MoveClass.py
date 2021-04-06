from tkinter import *

class MoveClass():
    def dragBinds():
        widget.bind("<ButtonPress-1>", self.startDrag)
        widget.bind("<B1-Motion>", self.drag)
        widget.bind("<ButtonRelease-1>", self.stopDrag)
        widget.configure(cursor="hand1")

    def startDrag(self, event):
        pass

    def drag(self, event):
        pass

    def stopDrag(self, event):
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass
