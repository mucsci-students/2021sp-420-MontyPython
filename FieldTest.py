import unittest
from ClassCollection import ClassCollection
from Class import Class
from Field import Field


class FieldTests(unittest.TestCase):

    # Checks if field is in the fieldDict
    def testAddField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        self.assertIsNotNone( collection.getField("A", "name"))

    # Checks if a field is successfully deleted
    def testDeleteField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        collection.deleteField("A", "name")
        self.assertIsNone( collection.getField("A", "name"))


     # Checks if a class is successfully deleted
    def testRenameField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        collection.renameField("A", "name", "surname")
        self.assertIsNotNone( collection.getField("A", "surname"))

    #rename Class with attributes. Ensure there is no leftover Class
    def testRenameFieldComplex(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        collection.renameField("A", "name", "surname")
        self.assertIsNone( collection.getField("A", "name"))
        self.assertRaises(KeyError, collection.addField, "A", "surname", "String")
        collection.deleteField("A", "surname")
        self.assertIsNone( collection.getField("A", "name"))
        self.assertIsNone( collection.getField("A", "surname"))

    #test error on adding duplicate classes
    def testAddDuplicateField(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addField("A", "name", "String")
        self.assertRaises(KeyError, collection.classDict["A"].addField, "name", "String")
    
    #test error on removing nonexisted classes
    def testRemoveNonExistentField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        self.assertRaises(KeyError, collection.deleteField,"A", "name")

    #test error on renaming duplicate classes
    def testRenameDuplicateField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        collection.addField("A", "surname", "String")
        self.assertRaises(KeyError,  collection.renameField,"A", "name", "surname")

    #test error on removing nonexisted classes
    def testRenameNonExistentField(self):
        collection = ClassCollection() 
        collection.addClass("A")
        collection.addField("A", "name", "String")
        collection.addField("A", "surname", "String")
        self.assertRaises(KeyError,  collection.renameField,"A", "joename", "surname")
   
if __name__ == '__main__':
    unittest.main()