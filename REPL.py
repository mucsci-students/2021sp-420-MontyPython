import Interface
from ClassCollection import ClassCollection
import sys
import os



# A default collection
collection = ClassCollection()

# Saves the file name of the most recently loaded or saved file
# Allows for use of save command without entering a file name
recentFile = ""

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
        first = False

    response = input(f'Please supply the following parameter(s): {paramString}\n')
    tokens = response.split()

    # If proper number of tokens are met, but requestParameters does not require a method's parameter list,
    # immediately returns tokens
    if len(tokens) >= length:
        return tokens
    # If not, recurses, requesting missing parameters
    else:
        start = len(tokens)
        tokens.append(requestParameters(paramList[start:]))

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
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Adds class
                collection.addClass(tokens[2])
            
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
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'field name', 'type']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Adds field
                collection.addField(tokens[2], tokens[3], tokens[4])

            # Add method takes three required parameters: class name, method name, return type
            # Add method may also take an even number of parameters after these three
            # The additional parameters alternate between parameter type and parameter name
            if obj == 'method':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'method name', 'return type']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                params = input(f"Please list any parameters for the method {tokens[3]}.\nEx: int foo int bar\n")
                paramsTokens = params.split()
                methodParameters = []
                for typ, name in zip(paramsTokens[0::2], paramsTokens[1::2]):
                    methodParameters.append((typ, name))
                # Adds method with appropriate parameter list
                collection.addMethod(tokens[2], tokens[3], tokens[4], methodParameters)

            # Add parameter takes two required parameters: class name, method name
            # From here, the user is asked which method by parameter list they would like to add to
            # Add parameter then takes two more required parameters: type and name
            if obj == 'parameter':
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                
                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    paramRaw = input("Please input the parameter type and name to be added:\n")
                    param = paramRaw.split()

                    if len(param) <= 1:
                        missing = 2 - len(tokens)
                        paramList = ['type', 'name']
                        start = len(paramList) - missing
                        addedTokens = requestParameters(paramList[start:])
                        tokens.extend(addedTokens)

                    collection.addParameter(tokens[2], tokens[3], methodParameters, param[0], param[1])

                else:
                    pass
            

        # ------- Delete ------- #
        elif tokens[0] == 'delete':
            obj = tokens[1].lower()

            # Delete class takes one parameter: name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) == 2:
                    missing = 3 - len(tokens)
                    paramList = ['name']
                    start = len(paramList) - missing
                    returnTokens = requestParameters(paramList[start:])
                    tokens.extend(returnTokens)
                # Deletes class
                collection.deleteClass(tokens[2])

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
                collection.deleteRelationship(tokens[2], tokens[3])

            # Delete field takes two parameters: class name, field name
            if obj == 'field':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'field name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Adds field
                collection.deleteField(tokens[2], tokens[3])

            # Delete method takes two required parameters: class name, method name
            # From here, the user is then asked which method they wish to delete by parameters
            if obj == 'method':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)

                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].split(", ")[1]

                    # Deletes method
                    collection.deleteMethod(tokens[2], tokens[3], methodParameters)

                else:
                    pass

        # ------- Rename ------- #
        elif tokens[0] == 'rename':
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
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'old field name', 'new field name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                # Renames field
                collection.renameField(tokens[2], tokens[3], tokens[4])

            # Rename method takes three required parameters: class name, old method name, new method name
            # From here, the user is asked which method they would like to rename from the parameters lists
            if obj == 'method':
                if len(tokens) <= 4:
                    missing = 5 - len(tokens)
                    paramList = ['class name', 'old method name', 'new method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)
                
                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    # Renames method
                    collection.renameMethod(tokens[2], tokens[3], methodParameters, tokens[4])

                else:
                    pass

        # ------- Remove ------- #
        elif tokens[0] == 'remove':
            obj = tokens[1].lower()

            # Remove parameter takes two required parameters: class name, method name
            # Then, it requests the user to select which method to remove from via its parameter list
            # Remove parameter then takes one more required parameter: name
            if obj == 'parameter':
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)

                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    delName = input("Please enter the name of the parameter you wish to remove.\n")
                    collection.removeParameter(tokens[2], tokens[3], methodParameters, delName)

                else:
                    pass

            # Remove parameters takes two required parameters: class name, method name
            # Then, it requests the user to select which method to remove via its parameter list
            # All parameters are then removed from this specific method
            if obj == 'parameters':
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)

                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    collection.removeAllParameters(tokens[2], tokens[3], methodParameters)

                else:
                    pass

        # ------- Change ------- #
        elif tokens[0] == 'change':
            obj = tokens[1].lower()

            # Change parameter takes two required parameters: class name, method name
            # Then, it requests the user to select which method to change via its parameter list
            # Change parameter then takes three more required parameters: old name, new type, new name
            if obj == 'parameter':
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)

                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    paramList = ['old name', 'new type', 'new name']
                    changeTokens = requestParameters(paramList)
                    collection.changeParameter(tokens[2], tokens[3], methodParameters, changeTokens[0], changeTokens[1], changeTokens[2])

                else:
                    pass

            # Change parameters takes two required parameters: class name, method name
            # Then, it requests the user to select which method to change via its parameter list
            # Change parameters then takes an arbitrary length list to tokenize into new parameters
            # The tokens should take the form type, name, type, name, so forth
            if obj == 'parameters':
                if len(tokens) <= 3:
                    missing = 4 - len(tokens)
                    paramList = ['class name', 'method name']
                    start = len(paramList) - missing
                    addedTokens = requestParameters(paramList[start:])
                    tokens.extend(addedTokens)

                parametersLists = collection.getMethodsByName(tokens[2], tokens[3])

                if parametersLists != None:
                    print(f"The following parameter lists have been found for the method {tokens[3]} in class {tokens[2]}:\n")
                    index = 0
                    for each in parametersLists:
                        print(f"{index}: {each}")
                        index += 1
                    
                    methodNum = int(input(f"Please select a parameter list by its number.\n"))
                    methodParameters = parametersLists[methodNum].parameters

                    paramListRaw = input(f"Please enter a new list of parameters.\n")
                    newParams = []
                    for typ, name in zip(paramListRaw[0::2], paramListRaw[1::2]):
                        newParams.append((typ, name))
                    collection.changeAllParameters(tokens[2], tokens[3], methodParameters, newParams)

                else:
                    pass

        # ------- List ------- #
        elif tokens[0] == 'list':
            obj = tokens[1].lower()

            # List class takes one parameter: class name
            if obj == 'class':
                # Finds number of missing parameters then calls requestParameters
                if len(tokens) == 2:
                    missing = 3 - len(tokens)
                    paramList = ['name']
                    start = len(paramList) - missing
                    returnTokens = requestParameters(paramList[start:])
                    tokens.extend(returnTokens)
                # Deletes class
                Interface.listClass(collection, tokens[2])

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
        elif tokens[0] == 'save':
            overwriteBool = True
            # If no file name is given and no recent file was saved or loaded,
            # requests file name from user
            if len(tokens) == 1 and recentFile == "":
                paramList = ['file name']
                returnTokens = requestParameters(paramList)
                tokens.extend(returnTokens)

            # Overwrite defaults to true. If there is no recent file, saves normally.
            # If there is a recent file and Y is selected, overwrites. If there is
            # a recent file and N is selected, does not save.
            
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
        elif tokens[0] == 'load':
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
        elif tokens[0] == 'help':
            Interface.help()

       # ------- Exit ------- #
       # Exit takes zero parameters
        elif tokens[0] == 'exit':
            Interface.exit()

        else:
            print('Invalid input. \nIf you would like to see input options, please type "help".\n')
        
    except (KeyError, ValueError, OSError, RuntimeError) as error:
        print(error)

    response = input('What would you like to do?\n')
    