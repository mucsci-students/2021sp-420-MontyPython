
class MoveClass:
    def __init__(self, controller, view, canvas):
        self.controller = controller
        self.view = view
        self.canvas = canvas

    def setBinds(self, className):
        self.canvas.tag_bind(className, '<ButtonPress-1>', lambda e, tag=className: self.startDrag(e, tag))
        self.canvas.tag_bind(className, '<B1-Motion>', lambda e, tag=className: self.drag(e, tag, className)) 
        self.canvas.tag_bind(className, '<ButtonRelease-1>', lambda e, tag=className: self.stopDrag(e, tag, className)) 
    
    # Starts move class drag
    def startDrag(self, event, tag):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    # Moves class with left click
    def drag(self, event, tag, className):
        widget = event.widget
        x = event.x - widget.startX
        y = event.y - widget.startY

        self.canvas.move(tag, x, y)
        self.view.classDict[className].updateCoordinateList()
        self.view.updateLineDict(className)
        widget.startX = event.x
        widget.startY = event.y

    def stopDrag(self, event, tag, className):
        widget = event.widget
        coordinates = self.canvas.coords(tag)
        x = coordinates[0]
        y = coordinates[1]
        self.view.classDict[className].updateAllCoordinates(x, y)
        self.view.drawLines()
        self.controller.updateClassCoordinates(className, x, y)