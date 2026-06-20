#Subscripting
print("Hello"[0]) #This says at 0th place of string hello is H
print("Hello"[-1]) # Means 1st character from last that is o


#integer = whole number
print(123 +345)

#large number
print(123_345_789)

#floating point number
print(3.1456 )

#Boolean


age = 28          # int
price = 19.99     # float
coords = 3 + 5j   # complex : : Stores numbers containing a real and imaginary part, designated by a j suffix.

print(age)
print(price)
print(coords)
#
# 3. Sequence Types
print("Sequence Data Type")
# list: An ordered, changeable collection that allows duplicate values.
# tuple: An ordered, unchangeable (immutable) collection that allows duplicates.
# range: Generates a sequence of numbers, commonly used in loops.

items = ["apple", "banana"]  # list
point = (10, 20)             # tuple
numbers = range(0, 10)       # range

print(numbers)
print(point)
print(items)

# Boolean Data Type
print("Boolean Data Type")
# Boolean data type represents one of two values: True or False.
# It is mainly used in conditions and comparisons and is represented by the bool class.
# type() checks the type of data
print(type(True))
print(type(False))

# Truthy and Falsy Values
print("Truthy and Falsy Values")
# truthy and falsy values are values that evaluate to True or False in a Boolean context.
# Truthy values behave like True, while falsy values behave like False when used in conditions.

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

# Set Data Type
print("Set Data Type")
# Sets are unordered and mutable collections used to store unique elements.
# Since sets are unordered, elements cannot be accessed using indexing.
# Elements are usually accessed by iterating through the set using a loop.

s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)

# Dictionary Data Type
print("Dictionary Data Type \n")
# Dictionaries are used to store data in key:value pairs.
# Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])
print(d.get(2))


#typecasting
print("\nTypeCasting \n")
print(int("123") + int("456"))


