import sys

arguments = path, command_name, db_name = sys.argv # this is called list unpacking in python
print(arguments)
print('''
You can print anything here.
You can even add a multiple lines 
''')

# path, arg1, arg2 = sys.argv
# print(sys.argv)
# print(f'Path: {path} arg1: {arg1} arg2: {arg2}')
# print(f' The command is {command_name.capitalize()} and the db name is {db_name.upper()} ')
