file = open('example.txt', 'w')  # Open a file in write mode

file.write('Hello, World!\n')  # Write a string to the file
file.write('This is an example of file handling in Python.\n')  # Write another

# opeing in write mode will overwrite the existing content of the file. If you want to append to the file instead, you can use 'a' mode.

# so we use error handling to handle the exception if the file does not exist or if there is an error while writing to the file.

try:
    file = open('example.txt', 'a')  # Open a file in append mode
    file.write('This line will be appended to the file.\n')  # Append a string to the file
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()  # Close the file to free up system resources
