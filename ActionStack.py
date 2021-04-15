from copy import deepcopy

class ActionStack():
    def __init__(self, Momento):
        #Entries in the stacks are Momento objects
        self.undoStack = []
        self.redoStack = []
        self.currentObj = deepcopy(Momento)
        self.originalObj = deepcopy(Momento)


    #Called when an undoable command (excluding undo/redo)
    #is called. Clears the redo stack to avoid illegal calls
    def add(self, Momento):
        self.undoStack.append(deepcopy(self.currentObj))
        self.currentObj = deepcopy(Momento)
        self.redoStack = []

    #Called when undo is called. Appends to redo stack
    def undoPop(self):
        if len(self.undoStack) == 0:
            print("No actions to undo")
            self.currentObj = deepcopy(self.originalObj)
        else:   
            self.redoStack.append(deepcopy(self.currentObj))
            self.currentObj = deepcopy(self.undoStack.pop())

            #Fringe case to fix being unable to remove a class added
            #if added immediately after returning to the original state
            if len(self.undoStack) == 0:
                self.currentObj = deepcopy(self.originalObj)

    #Called when redo is called. Appends to undo stack
    def redoPop(self):
        if len(self.redoStack) == 0:
            print("No actions to redo")
        else:
            self.undoStack.append(deepcopy(self.currentObj))
            self.currentObj = deepcopy(self.redoStack.pop())
        
    def reset(self, Momento):
        self.undoStack = []
        self.redoStack = []
        self.currentObj = deepcopy(Momento)
        self.originalObj = deepcopy(Momento)
