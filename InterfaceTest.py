import unittest
import os
import Interface
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
        with self.assertRaises(ValueError):
            Interface.saveFile(collection)       

    #WARNING: deletes file1.monty in current directory to ensure file creation
    def testCreatedSuccessfully(self):
        if os.path.isfile("file1.monty"):
            os.remove("file1.monty")
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        Interface.saveFile(collection, "file1")
        self.assertTrue(os.path.isfile("file1.monty"))

    def testSaveCorrectFileContents(self):
        comparisonString = "[{\"foo\": {}, \"bar\": {}}, {\"foo, bar\": {}}]"
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        Interface.saveFile(collection, "file2")
        with open("file2.monty", "r") as f:
            lines = f.readlines()
            print(lines[0])
            self.assertTrue((lines[0] == comparisonString) and (len(lines) == 1))

        
    def testLoadNoName(self):
        collection = ClassCollection()
        with self.assertRaises(ValueError):
            Interface.loadFile(collection)

    #WARNING: deletes file1.monty in current directory to ensure file does not exist
    def testLoadFileNotFound(self):
        collection = ClassCollection()
        if os.path.isfile("file1.monty"):
            os.remove("file1.monty")
        with self.assertRaises(OSError):
            Interface.loadFile(collection, "file1")   

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




        