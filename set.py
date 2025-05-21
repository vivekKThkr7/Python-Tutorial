# 3. Set : Unordered Mutable Collections of Unique Elements.
# Great for membership tests, eliminating duplicates, and set-theoretic operations.

# Creating Sets
empty_set = set()                   # empty_set == set()
singletons = {24}                   # singletons == {24}
fruits = {"Apple", "Orange", "Grapes"}

# Note: {} creates an empty dict; use set() for an empty set.

# Membership Tests
print("Banana" in fruits)           # Output: False
print("Orange" in fruits)           # Output: True

# Sets are unordered: you cannot index or slice
# fruits[0]                        # TypeError

# Adding & Removing Elements
fruits.add("Cherry")
print(fruits)                       # e.g. {'Grapes', 'Cherry', 'Apple', 'Orange'}

fruits.update(["Pineapple", "Mango"])
print(fruits)                       # e.g. {'Mango', 'Apple', 'Grapes', 'Cherry', 'Orange', 'Pineapple'}

# fruits.remove("Banana")          # Uncomment to see KeyError: 'Banana'
fruits.remove("Apple")
print(fruits)                       # e.g. {'Mango', 'Grapes', 'Cherry', 'Orange', 'Pineapple'}

fruits.discard("Mango")             # No error if not present
print(fruits)                       # e.g. {'Grapes', 'Cherry', 'Orange', 'Pineapple'}

popped = fruits.pop()               # Removes and returns an arbitrary element
print("Popped:", popped)            # e.g. Popped: 'Cherry'
print(fruits)                       # Remaining elements

# Clearing All Elements
# fruits.clear()
# print(fruits)                    # Output: set()

# Iterating Over a Set
for f in fruits:
    print("Fruit:", f)

# Set Comprehension
squares = {x**2 for x in range(10) if x % 2 == 0}
print(squares)                      # Output: {0, 4, 16, 36, 64}

# Set-Theoretic Operations
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print("Union:", a.union(b))         # {1, 2, 3, 4, 5, 6, 7}
print("Intersection:", a & b)       # {3, 4, 5}
print("Difference a - b:", a - b)   # {1, 2}
print("Difference b - a:", b - a)   # {6, 7}
print("Symmetric Diff:", a ^ b)     # {1, 2, 6, 7}

# Subset & Superset Tests
print({1, 2} <= a)                  # True  (subset)
print(a >= {2, 3})                  # True  (superset)
print(a.isdisjoint(b))              # False (they share elements)

# Converting Between Types
list_from_set = list(a)
print("List:", list_from_set)       # e.g. [1, 2, 3, 4, 5]

tuple_from_set = tuple(b)
print("Tuple:", tuple_from_set)     # e.g. (3, 4, 5, 6, 7)

# Frozenset: Immutable Version of Set
fs = frozenset([1, 2, 3])
# fs.add(4)                        # AttributeError: 'frozenset' object has no attribute 'add'
print("Frozenset:", fs)             # Output: frozenset({1, 2, 3})

# Real-World Use Case: Deduplicating a List
raw = [1, 2, 2, 3, 4, 4, 4]
unique = set(raw)
print("Unique items:", unique)      # Output: {1, 2, 3, 4}
