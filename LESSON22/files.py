import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt") # opens files; by default this is set to read
# print(f.read())
# print(f.read(4)) # Reads just the first 4 characters from the file based on where you are in the file.

# print(f.readline()) # Reads first line of the file
# print(f.readline()) # Reads the second line of the file (if being ran as a second)

# Similar to using .readline()
for line in f:
    print(line)

f.close() # Important to close the file after you finish using it.

try:
    f = open("names.txt") # Attempts to open the file
    print(f.read()) # Prints the file if it exists
except:
    print("The file you want to read doesn't exist.") # Error reported to user if the file doesn't exist.
finally:
    f.close() # If the file does exist and is opened, this will ensure it is closed once it is done.

# Append - creates the file if it doesn't exist
f = open("names.txt", "a") # must add "a" because by default open() is set to "r" = read.
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("jackson.txt"):
    f = open("jackson.txt", "x") # x = create
    f.close()

# Delete a file

# Avoid an error if it doesn't exist
if os.path.exists("jackson.txt"):
    os.remove("jackson.txt")
else:
    print("The file you wish to delete does not exist")

# This way of copying text from more_names.txt and overwriting the info into names.txt is more implicit
# rather than doing a try/except/finally block.

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)