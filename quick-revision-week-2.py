# Python Basics Revision Guide
# This script covers fundamental data structures and operations in Python.
# It includes definitions, examples, and explanations for a beginner learner.

# -------------------------------
# 1. Lists
# -------------------------------
# Definition:
# A list is an ordered, mutable (changeable) collection of items in Python.
# Lists can contain items of different types (e.g., numbers, strings, other lists).
#
# Example of a list:
fruits = ["apple", "banana", "cherry"]  # a list of strings
print(fruits)  # prints the whole list

# Accessing elements by index (starting at 0):
first_fruit = fruits[0]  # "apple"
print(first_fruit)  # prints "apple"

# Negative indexing: -1 refers to last element
print(fruits[-1])  # prints "cherry"

# Lists are mutable, so we can change elements:
fruits[1] = "blueberry"  # change second item from "banana" to "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

# Adding elements to a list:
fruits.append("date")  # adds "date" to the end of the list
print(fruits)  # now contains 4 items

# Inserting elements at a specific position:
fruits.insert(1, "banana")  # insert "banana" at index 1
print(fruits)  # "banana" is now back at index 1

# Removing elements:
fruits.remove("apple")  # removes "apple" from the list
print(fruits)  # "apple" is gone

# Removing by index:
del fruits[0]  # deletes the first element
print(fruits)

# Length of a list:
print(len(fruits))  # number of items in the list

# Check membership with 'in':
print("cherry" in fruits)  # True if "cherry" is in the list

# Slicing: get a sublist [start:stop]
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40], from index 1 up to (but not including) index 4

# Edge case: slicing beyond range doesn't cause an error, it just returns available items.
print(numbers[3:10])  # [40, 50] - stops at end

# Attempting to access an index that doesn't exist causes an IndexError:
# Uncommenting the next line would cause an error.
# print(numbers[10])  # IndexError: list index out of range

# Use case: Storing an ordered collection of items that can be changed as needed.

# -------------------------------
# 2. Tuples
# -------------------------------
# Definition:
# A tuple is an ordered, immutable (unchangeable) collection of items.
# Like lists, tuples can contain different data types, but once created,
# you cannot modify the elements of a tuple (no item assignment, add, remove).
#
# Example of a tuple:
person = ("Alice", 30, "Engineer")  # name, age, occupation
print(person)

# Accessing elements by index works like lists:
print(person[0])  # "Alice"
print(person[-1])  # "Engineer"

# Attempting to change a tuple element will cause an error (tuples are immutable):
# Uncommenting next line causes a TypeError.
# person[1] = 31

# Tuples are often used for fixed collections, e.g., returning multiple values from a function:
def get_point():
    # returns a tuple
    return (2, 3)
point = get_point()
x, y = point  # tuple unpacking
print(x, y)

# Single-element tuple needs a comma:
single_item_tuple = (42,)
not_a_tuple = (42)  # this is just an integer
print(type(single_item_tuple), type(not_a_tuple))  # <class 'tuple'> vs <class 'int'>

# Use case: Tuples can be used as keys in dictionaries (if they contain only hashable items)
location = {}
location[(10.0, 20.0)] = "Point A"  # (x, y) coordinate as a key

# -------------------------------
# 3. Sets
# -------------------------------
# Definition:
# A set is an unordered collection of unique items (no duplicates).
# Sets are mutable but only allow hashable (immutable) elements.
#
# Example of a set:
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # duplicates are removed, output: {1, 2, 3}

# Creating a set from a list (to remove duplicates):
nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3}

# Adding and removing elements:
unique_nums.add(4)
print(unique_nums)  # {1, 2, 3, 4}
unique_nums.remove(3)
print(unique_nums)  # {1, 2, 4}

# Edge case: Trying to remove an element not in the set causes a KeyError:
# Uncommenting next line causes KeyError.
# unique_nums.remove(10)

# Use discard to avoid error if element not present:
unique_nums.discard(10)  # no error if 10 is not in set

# Set operations: union, intersection, difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# Membership check is fast in sets:
print(2 in a)  # True

# Use case: Removing duplicates, membership testing, set algebra.

# -------------------------------
# 4. Dictionaries
# -------------------------------
# Definition:
# A dictionary is an unordered collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, or tuples),
# while values can be of any type.
#
# Example of a dictionary:
student = {"name": "John", "age": 21, "major": "Computer Science"}
print(student)

# Accessing values by key:
print(student["name"])  # "John"

# Adding or updating entries:
student["age"] = 22  # update age
student["GPA"] = 3.8  # add a new key-value pair
print(student)

# Removing entries:
del student["major"]
print(student)

# Edge case: Accessing a non-existent key causes a KeyError:
# Uncommenting next line causes KeyError.
# print(student["minor"])

# Use get() to avoid KeyError:
print(student.get("major"))  # None (since "major" was removed)
print(student.get("major", "Not declared"))  # default value if key not found

# Iterating over a dictionary:
for key in student:
    print(key, "=>", student[key])

# Or using items():
for key, value in student.items():
    print(key, ":", value)

# Use case: Fast lookups for values associated with unique keys (like a phonebook).

# -------------------------------
# 5. List Comprehension
# -------------------------------
# Definition:
# A concise way to create lists using a single line expression, typically involving a for-loop.
# Syntax: [expression for item in iterable if condition]
#
# Example: Create a list of squares of numbers from 0 to 9:
squares = [x**2 for x in range(10)]
print(squares)

# Equivalent with a loop:
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)
print(squares_loop)

# Adding a condition (filter): include only even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# List comprehension can include multiple loops:
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
print(pairs)  # Cartesian product-like pairs

# Edge case: List comprehensions can sometimes be less readable if too complex.
# Also, be cautious not to modify the list you are iterating over inside the comprehension.

# Use case: Quickly generate new lists based on existing iterables.

# -------------------------------
# 6. String Manipulation
# -------------------------------
# Definition:
# Strings are sequences of characters. They are immutable (cannot change characters in place).
#
# Example of a string:
text = "Hello, World!"
print(text)

# Accessing characters and slicing (like lists, index starts at 0):
print(text[0])    # 'H'
print(text[-1])   # '!'
print(text[7:12])  # 'World'

# Common string methods:
print(text.lower())   # all lowercase
print(text.upper())   # all uppercase
print(text.replace("World", "Python"))  # replace substring

# Splitting and joining:
words = text.split(", ")  # splits into list by delimiter
print(words)  # ['Hello', 'World!']
joined = "-".join(words)
print(joined)  # 'Hello-World!'

# Finding substrings:
print(text.find("World"))  # starting index of "World", 7
print(text.find("Python"))  # returns -1 if not found

# Edge case: Strings are immutable:
# Uncommenting next line causes a TypeError.
# text[0] = "h"

# String formatting:
name = "Alice"
age = 30
intro = f"My name is {name} and I am {age} years old."
print(intro)

# Use case: Text processing, user input/output formatting, working with lines of text.

# -------------------------------
# 7. Built-in Functions
# -------------------------------
# Definition:
# Python provides many built-in functions (no need to import) for various tasks.
#
# Examples of common built-ins:
print(len(text))    # returns the length of a sequence, e.g., string, list
print(type(text))   # returns the type of the object
print(int("123"))   # converts string to integer
print(str(456))     # converts number to string
print(max([1, 5, 2]))  # maximum in a list: 5
print(min([1, 5, 2]))  # minimum in a list: 1
print(sum([1, 2, 3]))  # sum of list elements: 6

# Range generates a sequence of numbers:
print(list(range(5)))  # [0, 1, 2, 3, 4]

# Enumerate pairs elements with index:
for index, value in enumerate(fruits):
    print(index, value)

# Zip can iterate over multiple sequences in parallel:
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
for letter, num in zip(letters, numbers):
    print(letter, num)

# Any and all:
print(any([True, False, True]))  # True if any element is True
print(all([True, False, True]))  # False, since not all are True

# Edge case: some built-ins can raise errors if used incorrectly:
# e.g., int("abc") would raise a ValueError.

# Built-ins also include: map, filter, sorted, reversed, etc.

