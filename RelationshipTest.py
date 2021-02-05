import unittest
from ClassCollection import ClassCollection

# Todo
# Check if the classes exist in the classCollection (helper?)
# Check if relationship already exists (helper?)
# if it does, error
# if not, add parameter pair to the relationshipCollection

class RelationshipTest(unittest.TestCase):
    def testAddRelationshipNoFirstClass(self):
        collection = ClassCollection()
        collection.addClass("foo")
        with self.assertRaises(KeyError, collection.addRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "bar does not exist")

    def testAddRelationshipNoSecondClass(self):
        collection = ClassCollection()
        collection.addClass("bar")
        with self.assertRaises(KeyError, collection.addRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "foo does not exist")
    
    def testAddRelationshipNeitherClassExist(self):
        collection = ClassCollection()
        with self.assertRaises(KeyError, collection.addRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "foo and bar do not exist")

    # Adding a relationship that already exists
    def testAddRelationshipAlreadyExists(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("bar", "foo")
        with self.assertRaises(KeyError, collection.addRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "Relationship bar, foo, already exists")

    def testRelationshipAddedSuccesfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        self.assertTrue(collection.checkRelationshipExists("foo", "bar"))

    def testDeleteRelationshipNoFirstClass(self):
        collection = ClassCollection()
        collection.addClass("foo")
        with self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "bar does not exist")

    def testDeleteRelationshipNoSecondClass(self):
        collection = ClassCollection()
        collection.addClass("bar")
        with self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "foo does not exist")
    
    def testDeleteRelationshipNeitherClassExist(self):
        collection = ClassCollection()
        with self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "foo and bar do not exist")

    # Adding a relationship that already exists
    def testDeleteRelationshipAlreadyExists(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.deleteRelationship("bar", "foo")
        with self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo") as contextManager:
            self.assertEqual(contextManager.exception.message, "Relationship bar, foo, already exists")

    def testRelationshipDeletedSuccesfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        self.assertTrue(collection.deleteRelationship("foo", "bar"))
        

if __name__ == '__main__':
    unittest.main()
    