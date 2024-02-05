# Python 101
print("Python 101")

# Variables and Data Types
print("\nI. Variables and Data Types")
# - no explicit type necessary
#   - identify type of a variable with type()
#   - cast a variable with int()
# - variables are case sensitive
## All Data Types
string = "string"
integer = 1
float = 1.0
list = ["contents", "of", "list"]
tuple = ("tuple1", "tuple2")
dictionary = {"word": 6}
boolean = True
range = range(6)
bytes = b"word"

# Numbers
print("\n\nII. Numbers")
# - Ints for round numbers
#   - Can type hexadecimal and Python will translate it to the corresponding integer 
# - Floats for decimal numbers
# - Complex for mix of numbers and letters
## Math
print(abs(integer)) # for absolute value
print(round(float)) # to round up floats
print(bin(integer)) # to convert to binary 
print(hex(integer)) # to convert to hexadecimal

# String formatting
print("\n\nIII. String Formatting")
# - Three " for multi-line string
## String operations
print(string * integer) # repeats the contents of string n times
print(len(string)) # gives number of characters in string
print("word" in string) # find occurrences of "word" in string, returns a bool
print(string.startswith("x")) # returns true or false if the string starts with the specified letter, returns a bool
print(string.index("s")) # finds where the word starts, returns an int
print(string.upper) # capitalizes the string
print(string.lower) # makes the string lower case
print(string.strip()) # prints without spaces
print(string.replace("a", "b")) # replaces a with b
print(string.split(",")) # splits string into a list, separated by commas
print(string.encode()) # encodes string using specified encoding
print(string.rjust(25)) # justifies string to the right by 25 characters
print(string.ljust(25)) # "                     " left "               "
print("string1" + "string2 " + str(integer)) # concatenation
## String formatting
print("String is {} characters long".format(len(string))) # can use .format as an easier way to concatenate
# {} in format can contain the index or variable name
# use {variable:datatype} to specify the datatype you want to be printed, or %d, %f, %x, etc.
print(f"Integer is {integer}") # string literal can place variables in the string without .format

# Booleans and Operators
print("\n\nIV. Booleans and Operators")
# - True or False
# != is the same as not var (can't use !var in Python)
# Use and/or to compare multiple statements
var = 10
boo = True
print(f"var: {var}")
print(f"boo: {boo}")
print("var >= 10 is " + str(var >= 10)) # returns True
print("var < 10 is " + str(var < 10)) # returns False
print("var > 5 and var < 15 is " + str(var > 5 and var < 15)) # returns True
print("boo == True returns " + str(boo == True)) # returns True
print("boo != True returns " + str(boo != True)) # returns False
print("not boo returns " + str(not boo)) # returns False
# floor division > num1 // num2
print("10 // 3 = " + str(10 // 3))