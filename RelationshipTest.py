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
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo")

    def testAddRelationshipNoSecondClass(self):
        collection = ClassCollection()
        collection.addClass("bar")
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo")
    
    def testAddRelationshipNeitherClassExist(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo")

    # Adding a relationship that already exists
    def testAddRelationshipAlreadyExists(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("bar", "foo")
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo")

    def testRelationshipAddedSuccesfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        self.assertIsNotNone(collection.getRelationship("foo", "bar"))

    def testDeleteRelationshipNoFirstClass(self):
        collection = ClassCollection()
        collection.addClass("foo")
        self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo")

    def testDeleteRelationshipNoSecondClass(self):
        collection = ClassCollection()
        collection.addClass("bar")
        self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo")
    
    def testDeleteRelationshipNeitherClassExist(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.deleteRelationship, "bar", "foo")

    def testRelationshipDeletedSuccesfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar")
        self.assertNotIn(("foo", "bar"), collection.relationshipDict)

if __name__ == '__main__':
    unittest.main()
    