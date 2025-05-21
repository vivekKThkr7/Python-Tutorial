# 2. Tuple : Ordered Immutable Sequences
# Like lists, but you cannot change (add/remove) elements once created.

# Creating Tuples
empty_tuple = ()
single = (42,)                  # Note the trailing comma—without it, (42) is just an int
person = ("Vivek", 24, True)

# Accessing elements
print(person[0])               # Output: Vivek
print(person[-1])              # Output: True

# Immutability: attempting to modify raises an error
# person[1] = 25               # TypeError: 'tuple' object does not support item assignment

# Tuple “methods” (only two because immutable)
print(person.count(True))      # Output: 1   — how many times True appears
print(person.index("Vivek"))   # Output: 0   — index of the first occurrence

# Tuple Packing & Unpacking
data = "Thakur", 25, False     # packing (parentheses optional)
name, age, is_student = data   # unpacking into variables
print(name, age, is_student)   # Output: Thakur 25 False

# Slicing (works exactly like lists)
letters = ('a', 'e', 'i', 'o', 'u')
print(letters[1:4])            # Output: ('e', 'i', 'o')
print(letters[::-1])           # Output: ('u', 'o', 'i', 'e', 'a')

# Concatenation and Repetition
nums = (1, 2, 3, 4)
print(nums)                    # Output: (1, 2, 3, 4)

more = nums + (5, 6, 7)
print(more)                    # Output: (1, 2, 3, 4, 5, 6, 7)

doubled = nums * 2
print(doubled)                 # Output: (1, 2, 3, 4, 1, 2, 3, 4)

# Converting between tuples and lists
list_from_tuple = list(nums)           # [1, 2, 3, 4]
tuple_from_list = tuple([9, 8])        # (9, 8)
