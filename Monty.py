import argparse
import subprocess

parser = argparse.ArgumentParser('')
parser.add_argument('--cli', action='store_true')
args = parser.parse_args()
argsDict = vars(args)

if argsDict['cli']:
    subprocess.run(['python', 'REPL.py'])
else:
    subprocess.run(['python', 'GUI.py'])
