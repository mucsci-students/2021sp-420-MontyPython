import unittest
from Method import Method
from ClassCollection import ClassCollection
from Class import Class

class ParameterTest(unittest.TestCase):
    # def addMethod(name, returnType):
    # def addParameter(method, paramList, type, name):
           
    def testAddParameterSuccessful(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "paramOne")
        self.assertIn(("int", "paramOne"), classA.methodDict["m1"][0].parameters)
    
    def testAddParameterSuccessfulPlural(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "string", "paramZero")
        classA.addParameter("m1", [("string", "paramZero")], "int", "paramOne")
        self.assertIn(("string", "paramZero"), classA.methodDict["m1"][0].parameters)
        self.assertIn(("int", "paramOne"), classA.methodDict["m1"][0].parameters)
    
    def testAddParameterNoType(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        self.assertRaises(KeyError, collection.addParameter("c1", "m1", [], "", "name"))
    
    def testAddParameterNoName(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        self.assertRaises(KeyError, collection.addParameter("c1", "m1", [], "int", ""))
    
    def testAddParameterInvalidMethod(self):
        classA = Class("c1")
        classA.addMethod("c1", "m1", "int")
        self.assertRaises(KeyError, classA.addParameter("badMethod", [], "int", "fail"))
    
    def testAddParameterAlreadyExists(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "string", "badString")
        self.assertRaises(KeyError, classA.addParameter("m1", [], "string", "badString"))
    # remove success (single)
    def testRemoveParameterSuccessful(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toRemove")
        classA.removeParameter("m1", [], "int", "toRemove")
        self.assertNotIn(("int", "toRemove"), classA.methodDict["m1"][0].parameters)
    
    def testRemoveParameterSuccessfulPlural(self):
        #
        pass
   
    def testRemoveParameterInvalidClass(self):
        #
        pass
    
    def testRemoveParameterInvalidMethod(self):
        #
        pass
    
    def testRemoveParameterNotFound(self):
        #
        pass
    # change success (single)
    def testChangeParameterSuccessfulSingle(self):
        #
        pass
    # change success (plural)
    def testChangeParameterSuccessfulPlural(self):
        #
        pass
    # change fail, class doesn't exist
    def testChangeParameterInvalidClass(self):
        #
        pass
    # change fail, method doesn't exist
    def testChangeParameterInvalidMethod(self):
        #
        pass
    # change fail, parameter not found
    def testChangeParameterNotFound(self):
        #
        pass

if __name__ == "__main__":
    unittest.main()