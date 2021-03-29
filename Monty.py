import argparse
import sys

parser = argparse.ArgumentParser('')
parser.add_argument('--cli', action='store_true')
args = parser.parse_args()
argsDict = vars(args)

if argsDict['cli']:
    from REPL import MontyREPL
    MontyREPL().cmdloop()
else:
    import GUI
