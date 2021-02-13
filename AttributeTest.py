import unittest
from ClassCollection import ClassCollection
from Class import Class

# Tests containing "FromCollection" refer to calling the wrapper function in
# ClassCollection.py, otherwise testing the function from Class.py

class AttributeTest(unittest.TestCase):
    # Checks if attribute is added successfully using Class.py addAttribute()
    def testAddValidAttribute(self):
        classA = Class("A")
        classA.addAttribute("count")
        self.assertIn("count", classA.getAttributes())

    # Checks if attribute is added successfully using ClassCollection.py addAttribute()
    def testAddValidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addAttribute("A", "count")
        self.assertIn("count", collection.getAttributes("A"))

    # Checks case of adding attribute that already exists through Class.py addAttribute()
    def testAddInvalidAttribute(self):
        classA = Class("A")
        classA.addAttribute("count")
        self.assertRaises(KeyError, classA.addAttribute, "count")

    # Checks case of adding attribute that already exists through ClassCollection.py addAttribute()
    def testAddInvalidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addAttribute("A", "count")
        self.assertRaises(KeyError, collection.addAttribute, "A", "count")

    # Checks if attribute is deleted successfully using Class.py deleteAttribute()
    def testDeleteValidAttribute(self):
        classA = Class("A")
        classA.addAttribute("date")
        classA.deleteAttribute("date")
        self.assertNotIn("date", classA.getAttributes())

    # Checks if attribute is deleted successfully using ClassCollection.py deleteAttribute()
    def testDeleteValidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addAttribute("A", "date")
        collection.deleteAttribute("A", "date")
        self.assertNotIn("date", collection.getAttributes("A"))

    # Checks case of trying to delete an attribute that doesn't exist using Class.py deleteAttribte()
    def testDeleteInvalidAttribute(self):
        classA = Class("A")
        self.assertRaises(KeyError, classA.deleteAttribute, "count")

    # Checks case of trying to delete an attribute that doesn't exist using ClassCollection.py deleteAttribte()
    def testDeleteInvalidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        self.assertRaises(KeyError, collection.deleteAttribute, "A", "count")
    
    # Checks if attribute is renamed successfully using Class.py renameAttribute()
    def testRenameValidAttribute(self):
        classA = Class("A")
        classA.addAttribute("oldName")
        self.assertIn("oldName", classA.getAttributes())
        classA.renameAttribute("oldName", "newName")
        self.assertIn("newName", classA.getAttributes())
        self.assertNotIn("oldName", classA.getAttributes())

    # Checks if attribute is renamed successfully using ClassCollection.py renameAttribute()
    def testRenameValidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        collection.addAttribute("A", "oldName")
        self.assertIn("oldName", collection.getAttributes("A"))
        collection.renameAttribute("A", "oldName", "newName")
        self.assertIn("newName", collection.getAttributes("A"))
        self.assertNotIn("oldName", collection.getAttributes("A"))

    # Checks case where attribute to rename does not exist when using Class.py renameAttribute()
    def testRenameInvalidAttribute(self):
        classA = Class("A")
        self.assertRaises(KeyError, classA.renameAttribute, "oldName", "newName")

    # Checks case where attribute to rename does not exist when using ClassCollection.py renameAttribute()
    def testRenameInvalidAttributeFromCollection(self):
        collection = ClassCollection()
        collection.addClass("A")
        self.assertRaises(KeyError, collection.renameAttribute, "A", "oldName", "newName")
    
    def testAddWithInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.addAttribute, "A", "someAttribute")
    
    def testRemoveWithInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.deleteAttribute, "A", "someAttribute")
    
    def testRenameWithInvalidClass(self):
        collection = ClassCollection()
        self.assertRaises(KeyError, collection.renameAttribute, "A", "oldAttributeName", "newAwesomeName")
    
if __name__ == '__main__':
    unittest.main()
