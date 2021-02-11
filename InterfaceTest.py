import unittest
import os
from Interface import Interface
from ClassCollection import ClassCollection

### Save test cases
    ## Did not supply file name
    ## Successful creation of file
    ## Compare contents of dumped file to what JSON output it should give

### Load test cases
    ## Did not supply file name
    ## File does not exist
    ## Check for equivalency before and after dumping to file then loading

class InterfaceTest(unittest.TestCase):
    def testSaveNoName(self):
        collection = ClassCollection()
        collection.addClass("foo")
        with self.assertRaises(KeyError, Interface.saveFile(collection)) as contextManager:
            self.assertEqual(contextManager.exception.message, "no file name given for save")        

    def testCreatedSuccessfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        self.assertTrue(Interface.saveFile(collection))

    def testSaveCorrectFileContents(self):

        comparisonString = "[{\"foo\": {}, \"bar\": {}}, {\"foo, bar\": {}}]"
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        Interface.saveFile(collection, "file1")
        with open("file1.monty", "r") as f:
            lines = f.readlines()
            self.assertTrue((lines[0] == comparisonString) and (len(lines) == 1))

        
    def testLoadNoName(self):
        with self.assertRaises(KeyError, Interface.loadFile()) as contextManager:
            self.assertEqual(contextManager.exception.message, "no file name given for load")
    
    def testLoadFileNotFound(self):
        collection = ClassCollection()
        collection.addClass("foo")
        Interface.saveFile(collection, "file1")
        with self.assertRaises(KeyError, Interface.saveFile(collection)) as contextManager:
            self.assertEqual(Interface.loadFile(collection, "file1"), "no file of given name found")    

    def testLoadCorrectFileContents(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        Interface.saveFile(collection, "file1")
        collectionLoaded = ClassCollection()
        Interface.loadFile(collectionLoaded, "file1")
        self.assertEqual(collection, collectionLoaded)

    
if __name__ == '__main__':
    unittest.main()




        