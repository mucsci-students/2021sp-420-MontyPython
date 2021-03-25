import unittest
from ClassCollection import ClassCollection
from Class import Class

class ClassTests(unittest.TestCase):

    # Checks if class is in the ClassDict
    def testAddClass(self):
        collection = ClassCollection() 
        collection.addClass("A")
        self.assertIsNotNone( collection.getClass("A"))

    # Checks if a class is successfully deleted
    def testDeleteClass(self):
        collection = ClassCollection()
        collection.addClass("A")
        #collection.addAttribute("A", "count")
        collection.deleteClass("A")
        self.assertRaises(KeyError, collection.getClass, "A")

     # Checks if a class is successfully deleted
    def testRenameClass(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.renameClass("A","B")
        self.assertIsNotNone(collection.getClass("B"))
    #rename Class with attributes. Ensure there is no leftover Class
    def testRenameClassComplex(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.renameClass("A","B")
      #  collection.addAttribute("B", "count")
        self.assertRaises(KeyError, collection.deleteClass, "A")
        self.assertIsNotNone( collection.getClass("B"))
        collection.deleteClass("B")
        self.assertRaises(KeyError, collection.getClass, "A")
        self.assertRaises(KeyError, collection.getClass, "B")

    #Ensure relations are also removed when a class is removed
    def testDeleteClassWithRelationship(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addClass("B")
        collection.addRelationship("A", "B", "composition")
        collection.deleteClass("A")
        self.assertRaises(KeyError, collection.getClass, "A")
        self.assertIsNotNone( collection.getClass("B"))
        self.assertEqual( collection.relationshipDict, {})

    #test error on adding duplicate classes
    def testAddDuplicateClass(self):
        collection = ClassCollection()
        collection.addClass("A")
        self.assertRaises(KeyError, collection.addClass, "A")
    
    #test error on removing nonexisted classes
    def testRemoveNonExistentClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.deleteClass, "A")

    #test error on renaming duplicate classes
    def testRenameDuplicateClass(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addClass("B")
        self.assertRaises(KeyError, collection.renameClass, "A", "B")

    #test error on removing nonexisted classes
    def testRenameNonExistentClass(self):
        collection = ClassCollection()
        collection.addClass("A")
        self.assertRaises(KeyError, collection.renameClass, "C", "D")

    def testDeleteClassWithRelationshipandField(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addClass("B")
        collection.addField("A", "name", "String")
        collection.addField("B", "name", "String")
        collection.addRelationship("A", "B", "composition")
        collection.deleteClass("A")
        collection.deleteClass("B")
        #Ok as long as there are no errors

if __name__ == '__main__':
    unittest.main()
