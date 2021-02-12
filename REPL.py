import Interface
from ClassCollection import ClassCollection

# A default collection
collection = ClassCollection()

response = ""
response = input('What would you like to do? \nType "Help" for options.\n')

while (response != 'exit'):
    response = response.lower()

    # ------- Class ------- #

    if response == 'add class':
        name = input('What would you like to name the class?\n')
        collection.addClass(name)
    
    elif response == 'delete class':
        name = input('What is the name of the class you would like to delete?\n')
        collection.deleteClass(name)

    elif response == 'rename class':
        oldName = input('What class would you like to rename?\n')
        newName = input('What would you like the new name to be?\n')
        collection.renameClass(oldName, newName)

    # ------- Relationship ------- #

    elif response == 'add relationship':
        source = input('What is the name of the source class?\n')
        destination = input('What is the name of the destination class?\n')
        collection.addRelationship(source, destination)

    elif response == 'delete relationship':
        source = input('What is the name of the source class?\n')
        destination = input('What is the name of the destination class?\n')
        collection.deleteRelationship(source, destination)
    
    # ------- Attribute ------- #

    elif response == 'add attribute':
        className = input('What is the name of the class the attribute belongs to?\n')
        attributeName = input ('What would you like to name the attribute?\n')
        collection.addAttribute(className, attributeName)

    elif response == 'delete attribute':
        className = input('What is the name of the class the attribute belongs to?\n')
        attributeName = input ('What is the name of the attribute?\n')
        collection.deleteAttribute(className, attributeName)
    
    elif response == 'rename attribute':
        className = input('What is the name of the class the attribute belongs to?\n')
        oldAttributeName = input('What attribute would you like to rename?\n')
        newAttributeName = input('What would you like the new name to be?\n')
        collection.renameAttribute(className, oldAttributeName, newAttributeName)
    
    # ------- Save/Load ------- #
    elif response == 'save':
        fileName = input('What would you like to name the file?\n')
        Interface.saveFile(collection, fileName)

    elif response == 'load':
        fileName = input('What is the name of the file you would like to load?\n')
        Interface.loadFile(collection, fileName)

    # ------- Interface ------- #
    elif response == 'list classes':
        Interface.listClasses(collection)
    
    elif response == 'list class':
        name = input('What is the name of the class?\n')
        Interface.listClass(collection, name)

    elif response == 'list relationships':
        Interface.listRelationships(collection)

    elif response == 'help':
        Interface.help()

    elif response == 'exit':
        Interface.exit()

    response = input('What would you like to do?\n')