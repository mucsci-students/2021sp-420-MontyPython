import unittest
import sys
import Interface
import io
from REPL import MontyREPL
from ClassCollection import ClassCollection
from Class import Class

class REPLTest(unittest.TestCase):
    def testListRelationships(self):
        repl = MontyREPL()
        repl.do_add_class('A')
        repl.do_add_class('B')
        repl.do_add_relationship('A B aggregation')

        oldStdOut = sys.stdout
        sys.stdout = newStdOut = io.StringIO()
        
        repl.do_list_relationships('A B')
        self.assertEqual(newStdOut.getvalue().strip(), 'A --> B (aggregation)')
        
        sys.stdout = oldStdOut
    
    @unittest.SkipTest
    def testListClasses(self):
        repl = MontyREPL()
        repl.do_add_class('A')
        repl.do_add_class('B')
        repl.do_add_class('C')
        
        oldStdOut = sys.stdout
        sys.stdout = newStdOut = io.StringIO()
        repl.do_list_classes('')

        testStr = ('A' + '\n------------------------\n\n' + 
                   'B' + '\n------------------------\n\n' + 
                   'C' + '\n------------------------' )

        self.assertEqual(newStdOut.getvalue().strip(), testStr)
        
        sys.stdout = oldStdOut
    
    #TODO: Update output when list class format gets updated
    @unittest.SkipTest
    def testListClass(self):
        repl = MontyREPL()
        repl.do_add_class('A')

        oldStdOut = sys.stdout
        sys.stdout = newStdOut = io.StringIO()
        repl.do_list_class('A')

        self.assertEqual(newStdOut.getvalue().strip(), 'A' + '\n' + '-'*24)

        sys.stdout = oldStdOut

    def testPostcmdSaveState(self):
        repl = MontyREPL()
        repl.do_add_class('A')
        repl.do_add_class('B')
        self.assertEqual(len(repl.saveStates.undoStack), 2)

    def testUndo(self):
        repl = MontyREPL()

        #undo an add command
        undoAddStrTest = "foo"
        repl.do_add_class("foo")
        repl.do_add_class("bar")
        repl.do_undo("")
        undoAddStr = ""
        for each in repl.model.classDict.keys():
            undoAddStr += each
        self.assertTrue(undoAddStrTest == undoAddStr)

        #undo a delete command
        undoDelStrTest = "('foo', 'bar')"
        repl.do_add_class("bar")
        repl.do_add_class("fizz")
        repl.do_add_relationship("foo bar aggregation")
        repl.do_add_relationship("foo fizz aggregation")
        repl.do_undo("")
        undoDelStr = ""
        for each in repl.model.relationshipDict.keys():
            undoDelStr += str(each)
        self.assertTrue(undoDelStrTest == undoDelStr)

        #undo a rename command
        undoRenStrTest = "('foo', 'test')"
        repl.do_rename_class("bar test")
        undoRenStr = ""
        for each in repl.model.relationshipDict.keys():
            undoRenStr += str(each)
        self.assertTrue(undoRenStrTest == undoRenStr)

        #undo when the most recent command cannot be undone
        #clears classes as order matters and this is not guaranteed
        #to add renamed classes to the end in the future
        repl.do_delete_class("foo")
        repl.do_delete_class("test")
        repl.do_delete_class("fizz")
        repl.do_add_class("foo")
        repl.do_add_class("bar")
        undoSkipStrTest = "foobar"
        repl.do_add_class("removed")
        repl.do_help("")
        repl.do_undo("")
        undoSkipStr = ""
        for each in repl.model.classDict.keys():
            undoSkipStr += each
        self.assertTrue(undoSkipStrTest == undoSkipStr)

    def testRedo(self):
        repl = MontyREPL()

        repl.do_add_class("foo")
        repl.do_add_class("bar")
        redoAddStrTest = ""
        for each in repl.model.classDict.keys():
            redoAddStrTest += each
        repl.do_undo("")
        repl.do_redo("")
        redoAddStr = ""
        for each in repl.model.classDict.keys():
            redoAddStr += each
        self.assertTrue(redoAddStrTest == redoAddStr)

        repl.do_delete_class("foo")
        redoDelStrTest = ""
        for each in repl.model.classDict.keys():
            redoDelStrTest += each
        repl.do_undo("")
        repl.do_redo("")
        redoDelStr = ""
        for each in repl.model.classDict.keys():
            redoDelStr += each
        self.assertTrue(redoDelStrTest == redoDelStr)

        repl.do_rename_class("bar fizz")
        redoRenStrTest = ""
        for each in repl.model.classDict.keys():
            redoRenStrTest += each
        repl.do_undo("")
        repl.do_redo("")
        redoRenStr = ""
        for each in repl.model.classDict.keys():
            redoRenStr += each
        self.assertTrue(redoRenStrTest == redoRenStr)