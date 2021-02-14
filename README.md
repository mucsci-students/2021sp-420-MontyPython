# CSCI 420 (Spring 2021) MontyPython UML Editor

## ----Not done yet----

This command line program creates a text representation of a UML diagram though user input. The program’s capabilities include adding, deleting, displaying, and modifying UML diagram elements. It also supports the ability to save and load diagrams.

## Prerequisites
To run the program, [Python 3.9.1](https://www.python.org/downloads/) needs to be installed.

## Running the program
1. Download the program from our [repository](https://github.com/mucsci-students/2021sp-420-MontyPython).
1. In a terminal, navigate to the directory our repository download has been saved in.
1. Type `Python REPL.py` to launch the command line program.
1. Follow the program’s prompts to create, load, or save a text representation of a UML diagram. Type `help` to view possible commands. 

### Example:  
![Example Image](https://i.imgur.com/3SAMIFe.png)

## Files
**Attribute.py:** Contains the “Attribute” class.

**Class.py:** Contains the “Class” class.

**ClassCollection.py:** Contains both the class dictionary and the relationship dictionary used to store the UML diagram. Also includes functions to add, delete, display, and modify UML elements. 

**Help.txt:** Contains the help text that displays when a user types ‘<help>’ in the terminal.
  
**Interface.py:** Contains code for save, load, and other interface functions.

**REPL.py:** The main file that contains code to prompt the user for input.

**RelationshipTest.py, AttributeTest.py, InterfaceTest.py, and ClassTest.py:** Contains unit tests for Class.py, ClassCollection.py, and Interface.py.

## Authors
[Quinn Lehman](https://github.com/qlehman)

[Joseph Malone](https://github.com/jmalone35)

[Drew Tuckey](https://github.com/aptuckey)

[Sean Malloy](https://github.com/sfmalloy)

[Jen Hynes](https://github.com/Jen04)
