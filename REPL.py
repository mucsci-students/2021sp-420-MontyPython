import cmd
import os
import sys
from colorama import init, Fore

from ClassCollection import ClassCollection
from Command import Command
from Momento import Momento
import Interface

if os.name == 'nt':
    import pyreadline
else:
    import readline

class MontyREPL(cmd.Cmd):
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        init(autoreset=True)
        self.saveStates = []
        self.classes = ClassCollection()
        self.intro = (Fore.GREEN + '\nMontyPython UML Editor\n' + '='*80 + 
            '\nType help [verbose|<command-name>] or ? for help on commands.\n')

        self.prompt = Fore.CYAN + 'monty> '
        dh = 'Type help [verbose|<command_name>] for descriptions'
        self.doc_header = dh

        # Read in Help.txt and extract every help description for every command.
        self.cmd_desc = {}
        with open('Help.txt') as help_doc:
            begin = 0
            lines = help_doc.readlines()
            while lines[begin][0] != '-':
                begin += 1

            lines = [lines[l].strip() for l in range(begin,len(lines))]
            l = 0
            while l < len(lines):
                if len(lines[l]) > 0 and lines[l][0] != '-':
                    command = lines[l]
                    desc = f'{command}\n'
                    l += 1
                    while l < len(lines) and len(lines[l]) > 0:
                        desc += f'    {lines[l]}\n'
                        l += 1
                    self.cmd_desc[command.split()[0]] = desc.rstrip()
                l += 1

    # Interface
    #
    # These are all standalone functions that don't affect the ClassCollection,
    # therefore there is no Command object created for any of these.
    def do_exit(self, args):
        Interface.exit()
    def do_help(self, args):
        if args == 'verbose':
            Interface.help()
        else:
            cmd.Cmd.do_help(self, args)
    def do_clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')
    def do_list_relationships(self, args):
        for rel in self.classes.relationshipDict:
            r = self.classes.relationshipDict[rel]
            print(f'{r.src} --> {r.dst} ({r.typ})')
    def do_list_classes(self, args):
        for c in self.classes.classDict:
            self.do_list_class(c)
    def do_list_class(self, args):
        c = args.split()[0]
        print(c)
        if len(self.classes.classDict[c].fieldDict) > 0:
            print('-'*24)
        for field in self.classes.classDict[c].fieldDict:
            print(f'  {self.classes.classDict[c].fieldDict[field]}')
        if len(self.classes.classDict[c].methodDict) > 0:
            print('-'*24)
        for method in self.classes.classDict[c].methodDict:
            for m in self.classes.classDict[c].methodDict[method]:
                print(f'  {m}')
        print('-'*24)
        print()
    def do_save(self, args):
        if len(args) > 0:
            Interface.saveFile(self.classes, args)
        else:
            self.help_save()
    def do_load(self, args):
        if len(args) > 0:
            Interface.loadFile(self.classes, args)
        else:
            self.help_load()

    # Classes
    def do_add_class(self, args):
        self.execute(self.classes.addClass, args)
    def do_delete_class(self, args):
        self.execute(self.classes.deleteClass, args)
    def do_rename_class(self, args):
        self.execute(self.classes.renameClass, args)

    # Relationships
    def do_add_relationship(self, args):
        self.execute(self.classes.addRelationship, args)
    def do_delete_relationship(self, args):
        self.execute(self.classes.deleteRelationship, args)
    def do_rename_relationship(self, args):
        self.execute(self.classes.renameRelationship, args)

    # Methods
    def do_add_method(self, args):
        args = args.split()
        params = []
        for i in range(3, len(args), 2):
            try:
                params.append([args[i], args[i + 1]])
            except IndexError:
                raise IndexError('Odd number of arguments for method parameters. '+ 
                'Method not added')
        args = args[:3] + [params]
        self.execute(self.classes.addMethod, args)
    def do_delete_method(self, args):
        args = args.split()
        methods = self.classes.getClass(args[0]).methodDict[args[1]]
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        self.execute(self.classes.deleteMethod, [args[0], args[1], methods[num].parameters])
    def do_rename_method(self, args):
        args = args.split()
        methods = self.classes.getClass(args[0]).methodDict[args[1]]
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        self.execute(self.classes.renameMethod, [args[0], args[1], methods[num].parameters, args[2]])

    # Fields
    def do_add_field(self, args):
        self.execute(self.classes.addField, args)
    def do_delete_field(self, args):
        self.execute(self.classes.deleteField, args)
    def do_rename_field(self, args):
        self.execute(self.classes.renameField, args)

    # Parameters
    def do_add_parameter(self, args):
        args = args.split()
        methods = self.classes.getClass(args[0]).methodDict[args[1]]
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        self.execute(self.classes.addParameter, [args[0], args[1], methods[num].parameters, args[2], args[3]])
        
    def do_delete_parameter(self, args):
        args = args.split()
        methods = self.classes.getClass(args[0]).methodDict[args[1]]
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        self.execute(self.classes.deleteParameter, [args[0], args[1], methods[num].parameters, args[2], args[3]])
        
    def do_change_parameters(self, args):
        args = args.split()
        methods = self.classes.getClass(args[0]).methodDict[args[1]]
        new_params = []
        for i in range(2, len(args), 2):
            new_params.append([args[i], args[i + 1]])
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        self.execute(self.classes.changeAllParameters, [args[0], args[1], methods[num].parameters, new_params])
        
    # help_cmd functions
    def do_verbose(self, args):
        self.do_help('verbose')
    def help_exit(self):
        self.print_cmd_help('exit')
    def help_help(self):
        self.print_cmd_help('help')
    def help_list_relationships(self):
        self.print_cmd_help('list_relationships')
    def help_list_classes(self):
        self.print_cmd_help('list_classes')
    def help_list_class(self):
        self.print_cmd_help('list_class')
    def help_clear(self):
        self.print_cmd_help('clear')

    def help_save(self):
        self.print_cmd_help('save')
    def help_load(self):
        self.print_cmd_help('load')

    def help_add_class(self):
        self.print_cmd_help('add_class')
    def help_delete_class(self):
        self.print_cmd_help('delete_class')
    def help_rename_class(self):
        self.print_cmd_help('rename_class')

    def help_add_relationship(self):
        self.print_cmd_help('add_relationship')
    def help_delete_relationship(self):
        self.print_cmd_help('delete_relationship')
    def help_rename_relationship(self):
        self.print_cmd_help('rename_relationship')

    def help_add_method(self):
        self.print_cmd_help('add_method')
    def help_delete_method(self):
        self.print_cmd_help('delete_method')
    def help_rename_method(self):
        self.print_cmd_help('rename_method')

    def help_add_field(self):
        self.print_cmd_help('add_field')
    def help_delete_field(self):
        self.print_cmd_help('delete_field')
    def help_rename_field(self):
        self.print_cmd_help('rename_field')

    def help_add_parameter(self):
        self.print_cmd_help('add_parameters')
    def help_delete_parameter(self):
        self.print_cmd_help('delete_parameters')
    def help_change_parameters(self):
        self.print_cmd_help('change_parameters')
    
    def help_verbose(self):
        print('verbose\nAlias for help verbose')

    # Helpers
    def print_cmd_help(self, command):
        print(self.cmd_desc[command])
    def postcmd(self, stop, line):
        pass
    def emptyline(self):
        pass
    def execute(self, function, args):
        if isinstance(args, str):
            args = args.split()
        command = Command(function, *args)
        command.execute()
        self.saveStates.append(Momento(command, self.classes))
    def onecmd(self, line):
        try:
            return super().onecmd(line)
        except Exception as e:
            if '()' not in str(e):
                print(e)
            else:
                print('Wrong number of arguments')
            self.print_cmd_help(line.split()[0])
            return False

if __name__ == '__main__':
    MontyREPL().cmdloop()
