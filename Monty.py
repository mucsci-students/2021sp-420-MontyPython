import argparse
import sys

parser = argparse.ArgumentParser('')
parser.add_argument('--cli', action='store_true')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()
argsDict = vars(args)

if argsDict['cli']:
    from REPL import MontyREPL
    MontyREPL().cmdloop()
elif argsDict['debug']:
    import GUI
    GUI.main(True)
else:
    import GUI
    GUI.main(False)


