#  Arithmetic Operators:
# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Modulus (remainder)
# ** Exponentiation
# // Floor division (returns the quotient, discarding the remainder)

print ("______Following are the Arithmetic Operators ______")

# can we take the value from user?
a = int(input("Enter the value of a\n")) # Value of a=10
b = int(input("Enter the value of b\n")) # Value of b=3

print ("______Addition______")
print(a+b)

print ("______Subtraction______")
print(a-b)

print ("______Multiplication______")
print(a*b)

print ("______Division______")
print(a/b) #10/3 = 3.3333333

print ("______Exponent Power______")
print(a**b) #10^3 = 10 * 10 * 10 = 1000

print ("_____Floor division (returns the quotient, discarding the remainder)_______")
print(a//b) # 10/3 0 -> 3.3 -> int -> 3 Q

print ("______Modulus(Remainder)______")
print(a%b) # 10% 3 = 1(remainder)