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
        self.assertEqual(len(repl.saveStates), 2)
