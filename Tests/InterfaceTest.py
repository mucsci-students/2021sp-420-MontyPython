import unittest
import os
import Interface
import filecmp
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

    #WARNING: deletes file1.monty in current directory to clean up after test
    #If the test is failing, comment out the final line of "os.remove("file1.monty")"
    #to manually check file contents
    def testCreatedSuccessfully(self):
        if os.path.isfile("file1.monty"):
            os.remove("file1.monty")
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "aggregation")
        Interface.saveFile(collection, "file1")
        self.assertTrue(os.path.isfile("file1.monty"))
        os.remove("file1.monty")

    #WARNING: deletes file1.monty in current directory to clean up after test
    #If the test is failing, comment out the final line of "os.remove("file1.monty")"
    #to manually check file contents
    #NOTE: test currently only checks for logic within save function
    #Once GUI coordinates are ironed out, update test with non-dummy coordinates
    #Will need to import GUI files to compare file's coordinates with actual ones
    def testSaveCorrectFileContentsGUI(self):
        comparisonString = "[{\"foo\": [{\"buzz\": [[\"int\", []], [\"int\", [[\"int\", \"a\"], [\"int\", \"b\"]]]]}, {\"test\": \"int\"}], \"bar\": [{}, {}]}, {\"foo, bar\": \"aggregation\"}, {\"foo\": [-2, -2], \"bar\": [-2, -2]}]"
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "aggregation")
        collection.addMethod("foo", "buzz", "int", [])
        collection.addMethod("foo", "buzz", "int", [("int", "a"), ("int", "b")])
        collection.addField("foo", "test", "int")
        Interface.saveFile(collection, "file1", "gui")
        with open("file1.monty", "r") as f:
            lines = f.readlines()
            self.assertTrue((lines[0] == comparisonString) and (len(lines) == 1))
        os.remove("file1.monty")

    #WARNING: deletes file1.monty in current directory to clean up after test
    #If the test is failing, comment out the final line of "os.remove("file1.monty")"
    #to manually check file contents
    def testSaveCorrectFileContentsCLI(self):
        comparisonString = "[{\"foo\": [{\"buzz\": [[\"int\", []], [\"int\", [[\"int\", \"a\"], [\"int\", \"b\"]]]]}, {\"test\": \"int\"}], \"bar\": [{}, {}]}, {\"foo, bar\": \"aggregation\"}, {\"foo\": [-1, -1], \"bar\": [-1, -1]}]"
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "aggregation")
        collection.addMethod("foo", "buzz", "int", [])
        collection.addMethod("foo", "buzz", "int", [("int", "a"), ("int", "b")])
        collection.addField("foo", "test", "int")
        Interface.saveFile(collection, "file1")
        with open("file1.monty", "r") as f:
            lines = f.readlines()
            self.assertTrue((lines[0] == comparisonString) and (len(lines) == 1))
        os.remove("file1.monty")

        
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

    #WARNING: deletes file1.monty and file2.monty in current directory to
    #clean up after test. If the test is failing, comment out the final lines of 
    #"os.remove("file1.monty")" and "os.remove("file2.monty")" 
    #to manually check file contents
    def testLoadCorrectFileContents(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "aggregation")
        collection.addMethod("foo", "buzz", "int", [])
        collection.addMethod("foo", "buzz", "int", [("int", "a"), ("int", "b")])
        Interface.saveFile(collection, "file1")
        collectionLoaded = ClassCollection()
        Interface.loadFile(collectionLoaded, "file1")
        Interface.saveFile(collectionLoaded, "file2")
        self.assertTrue(filecmp.cmp("file1.monty", "file2.monty"))
        os.remove("file1.monty")
        os.remove("file2.monty")

    
if __name__ == '__main__':
    unittest.main()




        