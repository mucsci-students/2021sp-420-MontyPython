import unittest
from Method import Method
from ClassCollection import ClassCollection
from Class import Class

# Note: for each test, test both functions from Class and ClassCollection (if applicable)

class MethodTest(unittest.TestCase):
    def testAddMethodSuccessful(self):
        # Class object function
        classA = Class("Person")
        classA.addMethod("age", "int")
        self.assertIn(("age", "int"), classA.methodDict)
        self.assertIn("", classA.methodDict)

        # ClassCollection function
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        self.assertIn(("getSpecies", "string"), collection.getClass("Animal").methodDict)

    def testAddMethodAlreadyExists(self):
        # Class object
        classA = Class("Person")
        classA.addMethod("age", "int")
        self.assertRaises(KeyError, classA.addMethod("age", "int"))

        # ClassCollection
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        self.assertRaises(KeyError, collection.addMethod("Animal", "getSpecies", "string"))

    def testAddMethodInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.addMethod("Animal", "getSpecies", "string"))

    def testDeleteMethodSuccessful(self):
        classA = Class("Person")
        classA.addMethod("age", "int")
        classA.deleteMethod("age", "int", "")
        self.assertNotIn(("age", "int"), self.methodDict)

        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "getSpecies", "string")
        collection.deleteMethod("Animal", "getSpecies", "string", "")

    def testDeleteMethodInvalidName(self):
        classA = Class("Person")
        self.assertRaises(KeyError, classA.deleteMethod("age", "int", ""))

        collection = ClassCollection()
        collection.addClass("Animal")
        self.assertRaises(KeyError, collection.deleteMethod("age", "int", ""))

    def testDeleteMethodInvalidType(self):
        classA = Class("Person")
        classA.addMethod("age", "unsigned")
        self.assertRaises(KeyError, classA.deleteMethod("age", "int", ""))
        
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "age", "unsigned")
        self.assertRaises(KeyError, collection.deleteMethod("age", "int", ""))

    def testDeleteMethodInvalidParams(self):
        classA = Class("Person")
        classA.addMethod("age", "unsigned")
        self.assertRaises(KeyError, classA.deleteMethod("age", "int", "year"))
        
        collection = ClassCollection()
        collection.addClass("Animal")
        collection.addMethod("Animal", "age", "unsigned")
        self.assertRaises(KeyError, collection.deleteMethod("age", "int", "year"))
    
    def testDeleteMethodInvalidClass(self):
        collection = ClassCollection()
        collection.addClass("Person")
        self.assertRaises(KeyError, collection.deleteMethod("Fish", "age", "int", "year"))

    def testRenameMethodSuccessful(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        classA.renameMethod("topping", "void", "", "addTopping")
        self.assertIn(("addTopping", "void"), classA.methodDict)
        self.assertNotIn(("topping", "void"), classA.methodDict)

        collection = ClassCollection()
        collection.addClass("Instrument")
        collection.addMethod("Instrument", "isNotPercussion", "bool")
        collection.renameMethod("Instrument", "isNotPercussion", "bool", "", "isWind")
        self.assertIn(("isWind", "bool"), collection.getClass("Instrument").methodDict)
        self.assertNotIn(("isNotPercussion", "bool"), collection.getClass("Instrument").methodDict)

    def testRenameMethodInvalidName(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        self.assertRaises(KeyError, classA.renameMethod("bruh", "void", "", "someOtherName"))

        collection = ClassCollection()
        collection.addClass("Instrument")
        self.assertRaises(KeyError, collection.renameMethod("Instrument", "bruh", "void", "", "newName"))

    def testRenameMethodInvalidType(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        self.assertRaises(KeyError, classA.renameMethod("topping", "bool", "", "setTopping"))

        collection = ClassCollection()
        collection.addClass("Instrument")
        collection.addMethod("Instrument", "isWind", "bool")
        self.assertRaises(KeyError, collection.renameMethod("Instrument", "isWind", "int", "", "newName"))

    def testRenameMethodInvalidParams(self):
        classA = Class("Pizza")
        classA.addMethod("topping", "void")
        self.assertRaises(KeyError, classA.renameMethod("topping", "void", "errorparm", "setTopping"))

        collection = ClassCollection()
        collection.addClass("Instrument")
        collection.addMethod("Instrument", "isWind", "bool")
        self.assertRaises(KeyError, collection.renameMethod("Instrument", "isWind", "bool", "error", "newName"))
    
    def testRenameMethodInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(collection.renameMethod("Instrument", "isWind", "bool", "", "isMayonaise"))

if __name__ == "__main__":
    unittest.main()