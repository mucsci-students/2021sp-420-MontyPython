'''
Usage: 
    Runs all tests: python RunTests.py
    Run one file:   python RunTests.py test_filename
'''

import unittest
import sys
import os

def runTest(name):
    test = f'Tests.{name.split(".")[0]}'
    __import__(test)
    unitTests = unittest.TestLoader().loadTestsFromModule(sys.modules[test])
    unittest.TextTestRunner(verbosity=2).run(unitTests)

if len(sys.argv) > 1:
    runTest(sys.argv[1])
else:
    _, _, filenames = next(os.walk("./Tests"))
    for test in filenames:
        if 'Test' in test:
            runTest(test)
        
