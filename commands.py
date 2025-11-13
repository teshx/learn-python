
# The Mini Command-Line Tool - Challenge
# Description
# You’ve just learned how to use sys.argv and conditional statements. Now it’s time to put that to work by creating your own mini command-line tool.

# Your Task
# Create a Python script called commands.py that behaves differently based on the command passed from the terminal.

# When you run the file from the command line, it should behave like this:

# python commands.py greet John
# # Output: Hello, John!
 
# python commands.py add 4 7
# # Output: The sum is 11.
 
# python commands.py help
# # Output: Available commands: greet, add, help
# ⚙️ Requirements
# Import the sys module.

# Use sys.argv to read command-line arguments.

# Check the number of arguments first — if fewer than 2, print:

# Please provide a valid command.
# Use if, elif, and else to handle different commands:

# greet <name> → print a personalized greeting.

# add <num1> <num2> → print the sum of two numbers.

# help → show a list of available commands.

# Handle missing arguments gracefully — don’t let the program crash.




# import sys

# print(sys.argv[1], sys.argv[2], sep=", ")
#    python commands.py greet John
# print(int(sys.argv[2]) + int(sys.argv[3]) )
#    python commands.py add 5 10

# print(f'available commands: greet, add, {sys.argv[1]}') 
# python commands.py help