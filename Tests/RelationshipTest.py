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
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo", "aggregation")

    def testAddRelationshipNoSecondClass(self):
        collection = ClassCollection()
        collection.addClass("bar")
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo", "aggregation")
    
    def testAddRelationshipNeitherClassExist(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo", "aggregation")

    # Adding a relationship that already exists
    def testAddRelationshipAlreadyExists(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("bar", "foo", "aggregation")
        self.assertRaises(KeyError, collection.addRelationship, "bar", "foo", "aggregation")

    def testRelationshipAddedSuccesfully(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "realization")
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
        collection.addRelationship("foo", "bar", "inheritance")
        collection.deleteRelationship("foo", "bar")
        self.assertNotIn(("foo", "bar"), collection.relationshipDict)
        self.assertRaises(KeyError, collection.deleteRelationship, "foo", "bar")

    def testRenameRelationship(self):
        collection = ClassCollection()
        collection.addClass("foo")
        collection.addClass("bar")
        collection.addRelationship("foo", "bar", "inheritance")
        collection.renameRelationship("foo", "bar", "composition")
        self.assertEquals("composition",collection.relationshipDict[("foo", "bar")].typ)
        
if __name__ == '__main__':
    unittest.main()
    