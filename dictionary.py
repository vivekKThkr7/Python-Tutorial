# 4. Dictionary : Unordered Mutable Mappings of Unique Keys to Values
# Ideal for fast lookups, grouping related data, and representing structured records.

# Creating Dictionaries
empty_dict = {}  
person = {
    "name": "Vivek",
    "age": 24,
    "is_student": True
}

# Accessing Values
print(person["name"])           # Output: Vivek
print(person.get("age"))        # Output: 24
print(person.get("grade", "N/A"))  # Output: N/A  (provides default if key missing)

# Modifying & Adding Entries
person["age"] = 25              # updates existing key
person["email"] = "vivek@example.com"  # adds new key
print(person)
# Output: {'name': 'Vivek', 'age': 25, 'is_student': True, 'email': 'vivek@example.com'}

# Removing Entries
age = person.pop("age")         # removes 'age', returns its value
print("Popped age:", age)       # Output: Popped age: 25

removed = person.pop("grade", None)  
print("Attempted pop missing key:", removed)  # Output: None

last = person.popitem()         # removes & returns an arbitrary (key, value) pair
print("Popped item:", last)

# Checking Keys, Values, Items
print("Keys:", person.keys())     # dict_keys([...])
print("Values:", person.values()) # dict_values([...])
print("Items:", person.items())   # dict_items([...])

# Iterating
for key in person:
    print(f"{key} → {person[key]}")

for key, val in person.items():
    print(f"{key} = {val}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(6)}
print(squares)                   # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging / Updating
defaults = {"theme": "light", "language": "en"}
overrides = {"language": "fr", "autosave": True}
defaults.update(overrides)
print(defaults)
# Output: {'theme': 'light', 'language': 'fr', 'autosave': True}

# Nesting Dictionaries
config = {
    "window": {"width": 800, "height": 600},
    "fullscreen": False
}
print(config["window"]["width"])  # Output: 800

# Converting to Other Types
keys_list = list(person.keys())
vals_list = list(person.values())
print("Keys list:", keys_list)
print("Values list:", vals_list)

# Clearing & Deleting
# person.clear()                # empties the dict
# del person["email"]           # removes that key

# Real-World Use Case: Counting Occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("Word counts:", counts)
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}
