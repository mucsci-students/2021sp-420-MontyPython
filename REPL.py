import cmd
import os
import sys
from functools import reduce
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
        self.model = ClassCollection()
        self.intro = (Fore.GREEN + '\nMontyPython UML Editor\n' + '='*80 + 
            '\nType help [verbose|<command-name>] or ? for help on commands.\n' + Fore.RESET)

        self.prompt = Fore.CYAN + 'monty> ' + Fore.RESET
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
        for rel in self.model.relationshipDict:
            r = self.model.relationshipDict[rel]
            print(f'{r.src} --> {r.dst} ({r.typ})')
    
    def do_list_classes(self, args):
        for c in self.model.classDict:
            self.do_list_class(c)
   
    # TODO: Edit the seperation lines to match the length of the longest
    #       line of text, with some pre-defined minimum length.
    def do_list_class(self, args):
        c = args.split()[0]
        name = f' {c}'
        fields = []
        methods = []
        for field in self.model.classDict[c].fieldDict:
            fields.append(f' {self.model.classDict[c].fieldDict[field]}')
        for method in self.model.classDict[c].methodDict:
            for m in self.model.classDict[c].methodDict[method]:
                methods.append(f' {m}')

        longest = max(15, len(max([name] + fields + methods, key=lambda s:len(s))))+1
        print_line = lambda l: print(f'|{l}{" "*max(1, longest-len(l))}|')
        print_sep = lambda: print(f'+{"-"*longest}+')

        print_sep()
        print_line(name)
        print_sep()

        if len(fields) > 0:
            for f in fields:
                print_line(f)
            print_sep()
        if len(methods) > 0:
            for m in methods:
                print_line(m)
            print_sep()

    def do_save(self, args):
        if len(args) > 0:
            Interface.saveFile(self.model, args)
        else:
            self.help_save()
    
    def do_load(self, args):
        if len(args) > 0:
            Interface.loadFile(self.model, args)
        else:
            self.help_load()

    # Classes
    def do_add_class(self, args):
        self.execute(self.model.addClass, args)
   
    def do_delete_class(self, args):
        self.execute(self.model.deleteClass, args)
   
    def do_rename_class(self, args):
        self.execute(self.model.renameClass, args)

    # Relationships
    def do_add_relationship(self, args):
        self.execute(self.model.addRelationship, args)
   
    def do_delete_relationship(self, args):
        self.execute(self.model.deleteRelationship, args)
    
    def do_rename_relationship(self, args):
        self.execute(self.model.renameRelationship, args)

    # Methods
    def do_add_method(self, args):
        args = args.split()
        if len(args) < 3:
            raise RuntimeError('Please include return type')
        params = []
        for i in range(3, len(args), 2):
            try:
                params.append([args[i], args[i + 1]])
            except IndexError:
                raise IndexError('Odd number of arguments for method parameters. '+ 
                'Method not added')
        args = args[:3] + [params]
        self.execute(self.model.addMethod, args)
   
    def do_delete_method(self, args):
        args = args.split()
        params = self.handle_overloaded_methods(args[0], args[1])
        self.execute(self.model.deleteMethod, [args[0], args[1], params])
    
    def do_rename_method(self, args):
        args = args.split()
        params = self.handle_overloaded_methods(args[0], args[1])
        self.execute(self.model.renameMethod, [args[0], args[1], params, args[2]])

    # Fields
    def do_add_field(self, args):
        self.execute(self.model.addField, args)
    
    def do_delete_field(self, args):
        self.execute(self.model.deleteField, args)
    
    def do_rename_field(self, args):
        self.execute(self.model.renameField, args)

    # Parameters
    def do_add_parameter(self, args):
        args = args.split()
        params = self.handle_overloaded_methods(args[0], args[1])
        self.execute(self.model.addParameter, [args[0], args[1], params, args[2], args[3]])
    
    def do_delete_parameter(self, args):
        args = args.split()
        params = self.handle_overloaded_methods(args[0], args[1])
        print(args[2])
        self.execute(self.model.removeParameter, [args[0], args[1], params, args[2]])
    
    def do_change_parameters(self, args):
        args = args.split()
        old_params = self.handle_overloaded_methods(args[0], args[1])
        new_params = []
        for i in range(2, len(args), 2):
            new_params.append([args[i], args[i + 1]])
        self.execute(self.model.changeAllParameters, [args[0], args[1], old_params, new_params])
        
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

    # Custom tab completion functions
    # To be able to autocomplete a new function
    #   1. Create a dict of int -> list of words that can be autocompleted
    #       based on the index of the argument (starting at 1)
    #   2. Pass all but begidx and endidx to self.arg_complete
    #
    # arg_completions is a dictionary of lists based on the index of the
    # current argument (including the command name, so starting at 1, 
    # similar to how sys.stdin works)
    def complete_list_class(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_list_relationships(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_delete_class(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)
    
    def complete_rename_class(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_add_relationship(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: list(self.model.classDict.keys()),
            3: ['aggregation', 'composition', 'inheritance', 'realization']
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_delete_relationship(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_rename_relationship(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: list(self.model.classDict.keys()),
            3: ['aggregation', 'composition', 'inheritance', 'realization']
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_add_method(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_delete_method(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getAllMethods(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_rename_method(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getAllMethods(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_add_field(self, text, line, begidx, endidx):
        arg_completions = {
            1: list(self.model.classDict.keys())
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_delete_field(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getFields(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_rename_field(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getFields(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_add_parameter(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getFields(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_delete_parameter(self, text, line, begidx, endidx):
        curr_args = line.split()

        # Only get method parameters if both the method and class exist.
        method_params = []
        if (len(curr_args) >= 3 and curr_args[1] in self.model.classDict
            and curr_args[2] in self.model.getAllMethods(curr_args[1])):
            for m in self.model.getMethodsByName(curr_args[1], curr_args[2]):
                param_names = [p[1] for p in m.parameters]
                method_params += param_names

        # Remove duplicate parameter names
        method_params = list(set(method_params))

        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getAllMethods(curr_args[1])),
            3: method_params
        }
        return self.arg_complete(text, line, arg_completions)

    def complete_change_parameters(self, text, line, begidx, endidx):
        curr_args = line.split()
        arg_completions = {
            1: list(self.model.classDict.keys()),
            2: ([] if len(curr_args) < 2 or curr_args[1] not in self.model.classDict
                    else self.model.getFields(curr_args[1]))
        }
        return self.arg_complete(text, line, arg_completions)
    
    # TODO: Use os.walk, and some fancy way of autocompleting directory paths
    # based on the user's OS...
    def complete_save(self, text, line, begidx, endidx):
        pass

    def complete_load(self, text, line, begidx, endidx):
        pass

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
        self.saveStates.append(Momento(command, self.model))
    
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
    
    def handle_overloaded_methods(self, className, methodName):
        methods = self.model.getMethodsByName(className, methodName)
        for method, idx in zip(methods, range(1, len(methods) + 1)):
            print(f'{idx}. {method}')
        num = int(input(Fore.CYAN + 'Method number: ')) - 1
        return methods[num].parameters

    # arg_complete -> list(str)
    # 
    # text: word being matched against
    # line: current line of input
    # arg_completions: dictionary of lists that contain valid words to
    #   autocomplete against based on the index of the current arg
    def arg_complete(self, text, line, arg_completions):
        idx = len(line.split())
        if text != '':
            idx -= 1
        if idx > len(arg_completions):
            return []
        return [arg for arg in arg_completions[idx] if arg.startswith(text)]

if __name__ == '__main__':
    MontyREPL().cmdloop()
