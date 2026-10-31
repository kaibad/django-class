# file handling using with statement in python.
# this is a better way to handle files in python as it automatically takes care of closing the file after the block of code is executed.

with open('example.txt', 'r') as file:  # Open a file in read mode
    content = file.read()  # Read the entire content of the file
    for line in content.splitlines():  # Split the content into lines and iterate over them
        print(line)  # Print each line of the file
