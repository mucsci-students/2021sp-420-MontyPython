class ActionStack():
    def __init__(self, Momento):
        #Entries in the stacks are Momento objects
        self.undoStack = []
        self.redoStack = []
        self.currentObj = Momento
        self.originalObj = Momento


    #Called when an undoable command (excluding undo/redo)
    #is called. Clears the redo stack to avoid illegal calls
    def add(self, Momento):
        self.undoStack.append(self.currentObj)
        self.currentObj = Momento
        self.redoStack = []

    #Called when undo is called. Appends to redo stack
    def undoPop(self):
        if len(self.undoStack) != 0:
            self.redoStack.append(self.currentObj)
            self.currentObj = self.undoStack.pop()
        else:
            self.currentObj = self.originalObj

    #Called when redo is called. Appends to undo stack
    def redoPop(self):
        if len(self.redoStack) != 0:
            self.undoStack.append(self.currentObj)
            self.currentObj = self.redoStack.pop()
            self.undoStack.append(self.currentObj)
        
    def reset(self, Momento):
        self.undoStack = []
        self.redoStack = []
        self.currentObj = Momento
        self.originalObj = Momento