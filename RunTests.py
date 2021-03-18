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
    res = unittest.TextTestRunner(verbosity=2, failfast=True).run(unitTests)
    if len(res.errors) > 0 or len(res.failures) > 0:
        exit(-1)

if len(sys.argv) > 1:
    runTest(sys.argv[1])
else:
    _, _, filenames = next(os.walk("./Tests"))
    for test in filenames:
        if 'Test' in test:
            runTest(test)
        
