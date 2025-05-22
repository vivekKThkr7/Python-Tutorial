 # Python Built-in Functions: Complete Guide with Examples

# 1. Basic I/O Functions
# print() - Output to console
print("Hello, Python!")  # Hello, Python!
print(1, 2, 3, sep="|", end="!\n")  # 1|2|3!

# input() - Get user input
name = input("Enter your name: ")
print(f"Welcome, {name}!")

# 2. Type Conversion
# int(), float(), str()
num_str = "25"
print(int(num_str) + 5)    # 30
print(float("3.14") * 2)   # 6.28
print(str(42) + " days")   # 42 days

# list(), tuple(), set(), dict()
nums = [1, 2, 2, 3]
print(tuple(nums))        # (1, 2, 2, 3)
print(set(nums))          # {1, 2, 3}
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# bool() - Truth value testing
print(bool(0))            # False
print(bool("Hello"))      # True

# 3. Mathematical Functions
# abs(), round(), divmod()
print(abs(-15))           # 15
print(round(3.14159, 2))  # 3.14
print(divmod(10, 3))      # (3, 1) - quotient and remainder

# sum(), min(), max()
nums = [4, 2, 9, 5]
print(sum(nums))          # 20
print(min(nums))          # 2
print(max(nums))          # 9

# pow() - Power function
print(pow(2, 3))          # 8
print(2 ** 3)             # 8 (equivalent)

# 4. Iteration and Sequence Handling
# range() - Number sequence
print(list(range(5)))      # [0, 1, 2, 3, 4]
print(list(range(2, 10, 3)))  # [2, 5, 8]

# enumerate() - Indexed iteration
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# zip() - Combine iterables
names = ['Alice', 'Bob']
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# reversed() - Reverse sequence
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# sorted() - Sorted version of iterable
nums = [3, 1, 4, 2]
print(sorted(nums))        # [1, 2, 3, 4]
print(sorted("python"))    # ['h', 'n', 'o', 'p', 't', 'y']

# 5. Functional Programming Tools
# map() - Apply function to items
nums = ["1", "2", "3"]
print(list(map(int, nums)))  # [1, 2, 3]

# filter() - Filter items by condition
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, range(10))))  # [0, 2, 4, 6, 8]

# Lambda functions
print(list(map(lambda x: x**2, range(5))))  # [0, 1, 4, 9, 16]

# any(), all() - Boolean checks
data = [True, False, True]
print(any(data))    # True
print(all(data))    # False

# 6. Object Introspection
# type(), isinstance()
x = 3.14
print(type(x))              # <class 'float'>
print(isinstance(x, float)) # True

# dir() - List attributes
print(dir([]))             # List of list methods

# id() - Memory address
a = [1, 2, 3]
print(id(a))               # Unique identifier

# 7. Advanced Functions
# eval(), exec() - Dynamic code execution (use with caution!)
x = 5
print(eval("x * 2"))       # 10

exec("y = 10\nprint(y*2)") # 20

# globals(), locals() - Namespace dictionaries
print(globals().keys())    # List of global variables

# 8. File Handling
# open() - File operations (always use with context manager)
with open('example.txt', 'w') as f:
    f.write("Hello\nWorld")

with open('example.txt') as f:
    print(f.read())        # Hello\nWorld

# 9. Real-World Examples
# 1. Data processing pipeline
data = ["5", "3.14", "10", "invalid"]
clean_data = [float(x) for x in data if x.replace('.', '').isdigit()]
print(clean_data)  # [5.0, 3.14, 10.0]

# 2. Temperature converter using map()
fahr = [32, 68, 100]
celsius = list(map(lambda f: (f-32)*5/9, fahr))
print(celsius)  # [0.0, 20.0, 37.777...]

# 3. Dictionary creation with zip()
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))  # {'a': 1, 'b': 2, 'c': 3}

# 10. Best Practices and Performance
# Prefer list comprehensions over map+lambda
# Good: [x**2 for x in range(5)]
# Less readable: list(map(lambda x: x**2, range(5)))

# Use generator expressions for large data
sum(x**2 for x in range(1000000))  # Memory efficient

# Use zip with strict=True (Python 3.10+) for equal length check
names = ['Alice', 'Bob']
scores = [85, 92]
try:
    list(zip(names, scores, strict=True))
except ValueError as e:
    print(e)

# Key Takeaways:
# 1. Use type conversion functions for data validation/transformation
# 2. Leverage zip/enumerate for cleaner iteration
# 3. Prefer list comprehensions over map/filter for simple cases
# 4. Use any()/all() for boolean aggregations
# 5. Be cautious with eval/exec - potential security risk
# 6. Always use context managers (with) for file handling
# 7. Use generator expressions for memory-efficient processing
