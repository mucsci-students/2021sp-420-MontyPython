import Interface
from ClassCollection import ClassCollection
import sys
import os

# Function for recursive calls when insufficient parameters are supplied
def requestParameters(paramList):
    length = len(paramList)
    paramString = ""
    first = True
    # Formats list of parameters into comma separated string
    for each in paramList:
        if first == False:
            paramString += ", "
        paramString += each
    response = input(f'Please supply the following parameter(s): {paramString}\n')
    tokens = response.split()
    # If proper number of tokens are met, returns token list
    if len(tokens) >= length:
        return tokens
    # If not, recurses, requesting missing parameters
    else:
        start = len(tokens)
        tokens.append(requestParameters(paramList[start:]))

# A default collection
collection = ClassCollection()

# Saves the file name of the most recently loaded or saved file
# Allows for use of save command without entering a file name
recentFile = ""

response = ""
response = input('What would you like to do? \nType "Help" for options.\n')
tokens = response.split()

while (tokens[0].lower() != 'exit'):
    # Forms list of individual words of input
    # As some commands are one, some are two, .lower() is used only on the first
    # If a second word for a command is needed, .lower() is used after identifying
    # which form of command it is
    tokens = response.split()
    tokens[0] = tokens[0].lower()

    try:
        # ------- Add ------- #
        if tokens[0] == 'add':
            obj = tokens[1].lower()

            # Add class takes one parameter: name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                # Note: for add class and other later functions with one parameter,
                # calling requestParameters is unnecessary. It is done for the sake
                # of consistency and code legibility.
                # To whomever updates this next, simplifying one parameter functions
                # will not break anything.
                if len(tokens) == 2:
                    missing = 3 - len(tokens)
                    paramList = ['name']
                    start = len(paramList) - missing
                    returnTokens = requestParameters(paramList[start:])
                # Adds class
                collection.addClass(returnTokens[0])
            
            # Add relationship takes three parameters: source class, destination class, type
            if obj == 'relationship':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['source class', 'destination class', 'type']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Adds relationship
                collection.addRelationship(tokens[2], tokens[3], tokens[4])

            # Add field takes three parameters: class name, field name, type
            if obj == 'field':
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'field name', 'type']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Adds field
                collection.addField(tokens[2], tokens[3], tokens[4])

            # Add method not yet implemented
            if obj == 'method':
                pass

        # ------- Delete ------- #
        if tokens[0] == 'delete':
            obj = tokens[1].lower()

            # Delete class takes one parameter: name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) == 2:
                    missing = 3 - len(tokens)
                    paramList = ['name']
                    start = len(paramList) - missing
                    returnTokens = requestParameters(paramList[start:])
                # Deletes class
                collection.deleteClass(returnTokens[0])

            # Delete relationship takes two parameters: source class, destination class
            if obj == 'relationship':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['source class', 'destination class']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Deletes relationship
                collection.addRelationship(tokens[2], tokens[3])

        # ------- Rename ------- #
        if tokens[0] == 'rename':
            obj = tokens[1].lower()

            # Rename class takes two parameters: old name, new name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['old name', 'new name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Renames class
                collection.renameClass(tokens[2], tokens[3])

            # Rename relationship takes three parameters: source class, destination class, type
            if obj == 'relationship':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['source class', 'destination class', 'type']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Renames class
                collection.renameRelationship(tokens[2], tokens[3], tokens[4])

            # Rename field takes three parameters: class name, old field name, new field name
            if obj == 'field':
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'old field name', 'new field name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Renames class
                collection.renameField(tokens[2], tokens[3], tokens[4])

            # Not yet implemented
            if obj == 'method':
                pass
        
        # ------- List ------- #
        if tokens[0] == 'list':
            obj = tokens[1].lower()

            # List class takes one parameter: class name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) == 2:
                    missing = 3 - len(tokens)
                    paramList = ['name']
                    start = len(paramList) - missing
                    returnTokens = requestParameters(paramList[start:])
                # Deletes class
                Interface.listClass(collection, returnTokens[0])

            # List classes takes zero parameters
            if obj == 'classes':
                Interface.listClasses(collection)

            # List relationships takes zero parameters
            if obj == 'relationships':
                Interface.listRelationships(collection)

        # ------- Save ------- #
        # Save takes one parameter: file name
        # If no name is given, but the file was previously loaded or saved,
        # the user is prompted if they wish to overwrite the file.
        if tokens[0] == 'save':
            # If no file name is given and no recent file was saved or loaded,
            # requests file name from user
            if len(tokens) == 1 and recentFile == "":
                paramList = ['file name']
                returnTokens = requestParameters[paramList]
                tokens.extend(returnTokens)

            # Overwrite defaults to true. If there is no recent file, saves normally.
            # If there is a recent file and Y is selected, overwrites. If there is
            # a recent file and N is selected, does not save.
            overwriteBool = True
            elif len(tokens) == 1 and os.path.isfile(recentFile):
                overwrite = input(f'Would you like to overwrite {recentFile}? Y/N\n')
                overwriteTokens = overwrite.split()
                if overwriteTokens[0].lower() == "n":
                    overwriteBool = False
                else:
                    tokens.append(recentFile)

            if overwriteBool == True:
                Interface.saveFile(collection, tokens[1])   

        # ------- Load ------- #
        # Load takes one parameter: file name
        if tokens[0] == 'load':
            # If file name is missing, requests name
            if len(tokens) == 1:
                paramList = ['file name']
                addedTokens = requestParameters(paramList)
                tokens.extend(addedTokens)
            # Updates recent file name to loaded file
            recentFile = tokens[1] + ".monty"
            # Loads file
            Interface.loadFile(collection, tokens[1])

        # ------- Help ------- #
        # Help takes zero parameters
        # Future update to allow for parsing individual commands for detailed help?
        if tokens[0] == 'help':
            Interface.help()

       # ------- Exit ------- #
       # Exit takes zero parameters
        if tokens[0] == 'exit':
            Interface.exit()

        else:
            print('Invalid input. \nIf you would like to see input options, please type "help".\n')
        
    except (KeyError, ValueError, OSError, RuntimeError) as error:
        print(error)

    response = input('What would you like to do?\n')
    