import unittest
from Method import Method
from ClassCollection import ClassCollection
from Class import Class

class ParameterTest(unittest.TestCase):
    
    def testAddParameterSuccessful(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", "int", "paramOne")
        self.assertIn("int paramOne", classA.methodDict["m1"])
    
    def testAddParameterSuccessfulPlural(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", "string", "paramZero")
        classA.addParameter("m1", "int", "paramOne")
        self.assertIn("string paramZero", classA.methodDict["m1"])
        self.assertIn("int paramOne", classA.methodDict["m1"])
    
    def testAddParameterNoType(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "int", "m1", "")
        self.assertRaises(KeyError, collection.addParameter("c1", "m1", "", "name"))
    
    def testAddParameterNoName(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "int", "m1", "")
        self.assertRaises(KeyError, collection.addParameter("c1", "m1", "int", ""))
    
    def testAddParameterInvalidMethod(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        self.assertRaises(KeyError, classA.addParameter("badMethod", "int", "fail"))
    
    def testAddParameterAlreadyExists(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", "string", "badString")
        self.assertRaises(KeyError, classA.addParameter("m1", "string", "badString"))
    # remove success (single)
    def testRemoveParameterSuccessful(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", "int", "toRemove")
        classA.removeParameter("m1", "int", "toRemove")
        self.assertNotIn(("int", "toRemove"), classA.methodDict["m1"])
    
    def testRemoveParameterSuccessfulPlural(self):
        pass
   
    def testRemoveParameterInvalidClass(self):
        pass
    
    def testRemoveParameterInvalidMethod(self):
        pass
    
    def testRemoveParameterNotFound(self):
        pass
    # change success (single)
    def 
    # change success (plural)

    # change fail, class doesn't exist

    # change fail, method doesn't exist

    # change fail, parameter not found
        
    # ("name", "type") -> methodClassList -(iterate to find specific one)-> parameterList
if __name__ == "__main__":
    unittest.main()