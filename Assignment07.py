# ------------------------------------------------- #
# Title: Assignment 07
# Description: Storing Data in a Binary File
# ChangeLog: (Michael Soha, Due May 31, 2022, Modified script for assignment)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# *** Working w/ Binary Files (Listing 9) *** #

# Pickling #

import pickle  # This imports code from another code file!

intCustomerID = str(input("Enter Customer ID: "))
strCustomerName = str(input("Enter Customer Name: "))
lstCustomer = [intCustomerID, strCustomerName]
print(lstCustomer)

# Now we store the data with the pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()

# And, we read the data back with the pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()

print(objFileData)

# *** Using Exception Class (Listing 12) *** #

# Error Handling #

try:
    f = open("AppData.dat", "rb")  # the read plus option gives an error if filed does not exist
except FileNotFoundError as e:
    print("Check that file exists!")
    print("Built-In Pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())


input()