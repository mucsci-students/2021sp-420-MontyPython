import unittest
from Method import Method
from ClassCollection import ClassCollection
from Class import Class

class ParameterTest(unittest.TestCase):
           
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

    # --------------------------------------------------------------------------------------------- #
    
    def testRemoveParameterSuccessful(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toRemove")
        classA.removeParameter("m1", [("int", "toRemove")], "toRemove")
        self.assertNotIn(("int", "toRemove"), classA.methodDict["m1"][0].parameters)
    
    
    def testRemoveParameterSuccessfulPlural(self):
        # A new list of parameters will replace the old
        # list of parameters.
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toRemove")
        classA.addParameter("m1", [("int", "toRemove")], "string", "toRemove2")
        classA.removeAllParameters("m1", [("int", "toRemove"), ("string", "toRemove2")])
        self.assertNotIn(("string", "toRemove2"), classA.methodDict["m1"][0].parameters)
        
   
    def testRemoveParameterInvalidClass(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        collection.addParameter("c1", "m1", [], "int", "integerOne")
        self.assertRaises(KeyError, collection.removeParameter("c2", "m1", [("int", "integerOne")], "integerOne"))
    
    def testRemoveParameterInvalidMethod(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        collection.addParameter("c1", "m1", [], "int", "integerOne")
        self.assertRaises(KeyError, collection.removeParameter("c1", "m2", [("int", "integerOne")], "integerOne"))
    
    def testRemoveParameterNotFound(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toRemove")
        self.assertRaises(KeyError, classA.removeParameter("m1", [("int", "toRemove")], "badParameter"))
    
    # -----------------------------------------------------------------------------------------------------------------------

    def testChangeParameterSuccessfulSingle(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toChange")
        classA.changeParameter("m1", [("int", "toChange")], "toChange", "string", "changed")
        self.assertIn(("string", "changed"), classA.methodDict["m1"][0].parameters)
    
    def testChangeParameterSuccessfulPlural(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toChange")
        classA.addParameter("m1", [("int", "toChange")], "double", "toChange2")
        classA.changeAllParameters("m1", [("int", "toChange"), ("double", "toChange2")], [("string", "newParam1"), ("int", "newParam2")])
        self.assertIn(("int", "newParam2"), classA.methodDict["m1"][0].parameters)
        self.assertNotIn(("int", "toChange"), classA.methodDict["m1"][0].parameters)
        
    
    def testChangeParameterInvalidClass(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        collection.addParameter("c1", "m1", [], "int", "integerOne")
        self.assertRaises(KeyError, collection.changeParameter("c2", "m1", [("int", "integerOne")], "integerOne", "string", "newParam"))
    
    def testChangeParameterInvalidMethod(self):
        collection = ClassCollection()
        collection.addClass("c1")
        collection.addMethod("c1", "m1", "int")
        collection.addParameter("c1", "m1", [], "int", "integerOne")
        self.assertRaises(KeyError, collection.changeParameter("c1", "m2", [("int", "integerOne")], "integerOne", "string", "newParam"))
    
    def testChangeParameterNotFound(self):
        classA = Class("c1")
        classA.addMethod("m1", "int")
        classA.addParameter("m1", [], "int", "toChange")
        self.assertRaises(KeyError, classA.changeParameter("m1", [("int", "toChange")], "badParameter", "string", "newParam"))

if __name__ == "__main__":
    unittest.main()