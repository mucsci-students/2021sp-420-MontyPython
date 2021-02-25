import unittest
from Method import Method
from ClassCollection import ClassCollection
from Class import Class

# Note: for each test, test both functions from Class and ClassCollection (if applicable)

class MethodTest(unittest.TestCase):
    def testAddMethodNoParams(self):
        # Class object function
        classA = Class("Person")
        classA.addMethod("age", "int")
        self.assertIn("age", classA.methodDict)

        # ClassCollection function
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        self.assertIn("getSpecies", collection.getClass("Animal").methodDict)
    
    def testAddMethodWithParams(self):
        classA = Class("Person")
        classA.addMethod("setName", "void", [("string", "newName")])
        self.assertIn("setName", classA.methodDict)
        self.assertIn(("string", "newName"), classA.methodDict["setName"][0].parameters)

        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "canEat", "bool", [("double", "timeSinceLastAte")])
        self.assertIn("canEat", collection.classDict["Animal"].methodDict)
        self.assertIn(("double", "timeSinceLastAte"), collection.classDict["Animal"].methodDict["canEat"].parameters)
    
    def testAddMethodAlreadyExists(self):
        # Class object w/ no params
        classA = Class("Person")
        classA.addMethod("age", "int")
        self.assertRaises(KeyError, classA.addMethod("age", "int"))

        # Class object w/ params
        classB = Class("Pizza")
        classB.addMethod("addCheese", "void", ("string", "cheese"))
        self.assertRaises(KeyError, classB.addMethod("addCheese", "void", ("string", "cheese")))

        # ClassCollection
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        self.assertRaises(KeyError, collection.addMethod("Animal", "getSpecies", "string"))

    def testAddMethodInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.addMethod("Animal", "getSpecies", "string"))

    def testDeleteMethodSuccessful(self):
        # Class object, no params, single method
        classA = Class("Person")
        classA.addMethod("age", "int")
        classA.deleteMethod("age", [])
        self.assertNotIn("age", classA.methodDict)

        # TODO: Class object, multiple overloaded methods
        classB = Class("Pizza")
        classB.addMethod("addCheese", "void", [("string", "type")])
        classB.addMethod("addCheese", "void", [("string", "type"), ("int", "amount")])

        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        collection.deleteMethod("Animal", "getSpecies", [])
        self.assertNotIn("getSpecies", "string")

    def testDeleteMethodInvalidName(self):
        classA = Class("Person")
        self.assertRaises(KeyError, classA.deleteMethod("age", []))

        collection = ClassCollection()
        collection.addClass("Animal")
        self.assertRaises(KeyError, collection.deleteMethod("Animal", "age", []))

    def testDeleteMethodInvalidParams(self):
        classA = Class("Person")
        classA.addMethod("age", "unsigned")
        self.assertRaises(KeyError, classA.deleteMethod("age", [("int", "year")]))
        
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "age", "unsigned")
        self.assertRaises(KeyError, collection.deleteMethod("Animal", "age", [("int", "year")]))
    
    def testDeleteMethodInvalidClass(self):
        collection = ClassCollection()
        collection.addClass("Person")
        self.assertRaises(KeyError, collection.deleteMethod("Fish", "age", [("int", "year")]))

    def testRenameMethodSuccessful(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        classA.renameMethod("topping", [], "addTopping")
        self.assertIn("addTopping", classA.methodDict)
        self.assertNotIn("topping", classA.methodDict)

        collection = ClassCollection()
        collection.addClass("Instrument")
        collection.addMethod("Instrument", "isNotPercussion", "bool")
        collection.renameMethod("Instrument", "isNotPercussion", [], "isWind")
        self.assertIn("isWind", collection.getClass("Instrument").methodDict)
        self.assertNotIn("isNotPercussion", collection.getClass("Instrument").methodDict)

    def testRenameMethodInvalidName(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        self.assertRaises(KeyError, classA.renameMethod("bruh", [], "someOtherName"))

        collection = ClassCollection()
        collection.addClass("Instrument")
        self.assertRaises(KeyError, collection.renameMethod("Instrument", "bruh", [], "newName"))

    def testRenameMethodInvalidParams(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        self.assertRaises(KeyError, classA.renameMethod("topping",  [("int", "errorparm")], "setTopping"))

        collection = ClassCollection()
        collection.addClass("Instrument")
        collection.addMethod("Instrument", "isWind", "bool")
        self.assertRaises(KeyError, collection.renameMethod("Instrument", "isWind", [("void*", "error")], "newName"))
    
    def testRenameMethodInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(collection.renameMethod("Instrument", "isWind", [], "isMayonaise"))

if __name__ == "__main__":
    unittest.main()