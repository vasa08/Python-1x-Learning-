# String : String is a Bunch of Characters
name = "pramod"
name = "dutta"

# String Functions
# Python String Immutable in Nature - They can't changed!, One Created
# name[0] = "h" # TypeError: 'str' object does not support item assignment

print("________Capitalize Function_______")

# capitalize() :  Returns a copy of the string with its first character capitalized.
result = name.capitalize() # Out put :  Dutta
print(result) # Out put :  Dutta
print(name) # Out put :  dutta

print(id(name))
print(id(result))

print("________UPPER CASE Function_______")

# Upper Case : Returns a copy of the string with its all character as uppercase.
result2 = name.upper() # Out put :  DUTTA
print(result2)

print("____LOWER CASE Function_______")

# Lower : Returns a copy of the string with its all character as lowercase.
result3 = name.lower() # Out put :  dutta
print(result3)

print("________Identity Function__________")
print(id(result3))  # Identity - Address Ref.

print("____SWAPCASE Function_______")
# Swapcase() : Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
name = "pRaMoD"
print(name.swapcase()) # Out Put : PrAmOd


print("____TITLE Function_____")
# Title
# Returns a titlecased version of the string,
# where words start with an uppercase character and  the remaining characters are lowercase.

name = "heLLo woRlD" # Name as hello world/ HeLLo WoRlD /  hEllo World
print(name.title())

print("____Capitalize and Uppercase Function_____")
t1 = "dutta ji"
t2 = "pramod ji"
print(t1.capitalize()) # # capitalize() :  Returns a copy of the string with its first character capitalized.
print(t2.upper()) #Upper Case : Returns a copy of the string with its all character as uppercase.

# t1 is ref or variable name ,  "dutta ji" which is stored in memory

print ("____Length Of String___ ")
name = "dutta"
print(len(name))

print ("____Replace Of String___ ")
# Replace
text = "hello world"
result_rep = text.replace("world","Python")
print(result_rep)


print ("____Length & Index Of String___ ")
#index and len
name  = "pramod"
# len -> 1
print(len(name))
# index - 0 to len-1
# p - 0, r - 1, a - 2, m - 3 , 0-4, d -5

print ("______Find Function _____ ")
#find()
#Returns the lowest index of a substring in the string.
# Returns -1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)



#count() - count the char -
count = text.count("l")
print(count)


name  = "p d"
print(len(name))


name= "pramod"
print(name)
del name
print(name)