def main(debug):   
    import sys
    import GUIController
    import ClassCollection
    import tkinter as tk
    from GUIMainWindow import MainWindow

    model = ClassCollection.ClassCollection()

    # App instance
    root = tk.Tk()
    # Size
    root.geometry("1000x900")
    # Instance of main window
    window = MainWindow(root)

    controller = GUIController.GUIController(model, window, debug)

    # Main loop for window
    root.mainloop()



