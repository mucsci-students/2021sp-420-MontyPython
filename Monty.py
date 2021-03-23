import argparse
import sys

try:
    import PyQt5
except ImportError:
    print('Please run Install.py for required packages')
    exit()

parser = argparse.ArgumentParser('')
parser.add_argument('--cli', action='store_true')
args = parser.parse_args()
argsDict = vars(args)

if argsDict['cli']:
    from REPL import MontyREPL
    MontyREPL().cmdloop()
else:
    import GUI
