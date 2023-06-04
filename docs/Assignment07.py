# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Using pickling to store data in binary format and load it back
#              into the script. Using try-except to demonstrate structured
#              error handling.
# ChangeLog (Who,When,What):
# MCambra,6.3.2023,Created script
# ---------------------------------------------------------------------------- #

# Pickling Demo #
print("1. Let's look at a Pickling Demo")

import pickle  # This imports code from another code file!

# Create an inventory list with item and count from user input
item_name = str(input("Enter an Item: "))
count = int(input("Enter the number owned: "))
inventory = [item_name, count]
print("Here is what you input to the inventory: ", inventory)

# Store the data in binary format with the pickle.dump method
objFile = open("InventoryData.dat", "ab")
pickle.dump(inventory, objFile)
objFile.close()

# Read the data back with the pickle.load or unpickling method
objFile = open("InventoryData.dat", "rb")
objFileData = pickle.load(objFile) # load() only loads one row of data.
objFile.close()

print("Here is the first inventory item and its count from the file: ", objFileData)
print()

# Structured Error Handling Demo
print("2. Now let's try structured error handling in Python")

# The piece of code we are trying that will not throw a python error if it fails
# Here we are allowing the user to input a file name
try:
    file_name = input("Input a file name (with extension) that doesn't exist: ")
    f = open(file_name, 'r')
    f_data = f.readlines()
    f.close()
    print(f_data)

# Except statement allows the coder to decide what error to display
except Exception as e:
    print("This file doesn't exist")
    print("Built-In Pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())