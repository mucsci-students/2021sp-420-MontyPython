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
    results = unittest.TextTestRunner().run(unitTests)
    fails = len(results.failures)
    errors = len(results.errors)
    return fails, errors

fails = 0
errors = 0

if len(sys.argv) > 1:
    runTest(sys.argv[1])
else:
    _, _, filenames = next(os.walk("./Tests"))
    for test in filenames:
        if 'Test' in test:
            f, e = runTest(test)
            fails += f
            errors += e 
    if fails > 0 or errors > 0:
        print('-'*70)
        print(f'FAILS: {fails}')
        print(f'ERRORS: {errors}')
        print('Exiting with status -1')
        exit(-1)
    else:
        print('ALL TESTS PASSED')

        
