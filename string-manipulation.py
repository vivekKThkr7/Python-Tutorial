# String Manipulation in Python: Complete Guide with Examples

# 1. Basic String Operations
# Strings are immutable sequence of Unicode characters

# Creating strings
single_quoted = 'Hello World'
double_quoted = "Python Programming"
multiline = '''This is a
multi-line string'''
print(multiline)

# Concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World

# Repetition
stars = "*" * 10
print(stars)  # **********

# 2. String Indexing and Slicing
text = "Pythonista"

# Indexing (0-based)
print(text[0])   # P
print(text[-1])  # a (last character)

# Slicing [start:end:step]
print(text[2:6])    # thon
print(text[::2])    # Ptoit (every 2nd character)
print(text[::-1])   # atsinohtyP (reverse)

# 3. Common String Methods
# Case manipulation
s = "Hello Python"
print(s.upper())       # HELLO PYTHON
print(s.lower())       # hello python
print(s.title())       # Hello Python
print(s.swapcase())    # hELLO pYTHON

# Stripping whitespace
text = "   spaces around   \t\n"
print(text.strip())    # "spaces around"
print(text.lstrip())   # "spaces around   \t\n"
print(text.rstrip())   # "   spaces around"

# 4. String Searching and Validation
msg = "Python version 3.11.4"

# Check start/end
print(msg.startswith("Python"))  # True
print(msg.endswith(".4"))        # True

# Finding substrings
print(msg.find("ver"))      # 7 (index)
print(msg.index("3"))       # 14
print("version" in msg)     # True

# Character checks
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("Python3".isalnum())  # True

# 5. String Formatting
# Old-style formatting
print("Name: %s, Age: %d" % ("Alice", 30))  # Name: Alice, Age: 30

# str.format()
print("{} + {} = {}".format(2, 3, 5))       # 2 + 3 = 5
print("{1} comes before {0}".format("Z", "A"))  # A comes before Z

# f-strings (Python 3.6+)
name = "Bob"
age = 25
print(f"{name} is {age} years old")         # Bob is 25 years old
print(f"Hex: {255:#x}, Binary: {10:b}")     # Hex: 0xff, Binary: 1010

# 6. String Splitting and Joining
# Splitting
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Joining
lines = ["First line", "Second line", "Third line"]
print("\n".join(lines))  # Multi-line output

# Partitioning
email = "user@domain.com"
local, _, domain = email.partition("@")
print(f"Local: {local}, Domain: {domain}")  # Local: user, Domain: domain.com

# 7. Advanced Formatting
# Format specifications
print(f"{3.1415926:.2f}")       # 3.14
print("{:>10}".format("right"))  # "     right"
print("{:_^15}".format("center")) # ___center____

# Template strings (safe substitution)
from string import Template
t = Template("Hello $name! Your balance: $$ $amount")
print(t.substitute(name="Alice", amount=100.5))  # Hello Alice! Your balance: $ 100.5

# 8. Regular Expressions (Regex)
import re

# Basic pattern matching
text = "Contact: email@example.com, phone: 123-456-7890"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)  # ['email@example.com']

# Substitution
masked = re.sub(r'\d', 'X', "Card: 1234-5678-9012-3456")
print(masked)  # Card: XXXX-XXXX-XXXX-XXXX

# 9. String Translation
# Character translation table
trans_table = str.maketrans('aeiou', '12345')
text = "hello world"
print(text.translate(trans_table))  # h2ll4 w4rld

# 10. Encoding/Decoding
# String to bytes
text = "Python 🐍"
encoded = text.encode('utf-8')
print(encoded)  # b'Python \xf0\x9f\x90\x8d'

# Bytes to string
decoded = encoded.decode('utf-8')
print(decoded)  # Python 🐍

# 11. Advanced Techniques
# String interpolation with format_map
data = {'name': 'Charlie', 'score': 95}
print("{name} scored {score}%".format_map(data))  # Charlie scored 95%

# Using zfill for numeric padding
print("42".zfill(5))        # 00042
print("-3.14".zfill(10))    # -00003.14

# 12. Performance Considerations
# Concatenation in loops (bad practice)
result = ""
for i in range(1, 5):
    result += str(i)  # Creates new string each time

# Better approach using list + join()
parts = []
for i in range(1, 5):
    parts.append(str(i))
print("".join(parts))  # 1234

# 13. Real-World Examples
# 1. CSV parsing
csv_line = "2023-07-25,Python Workshop,50"
date, event, capacity = csv_line.split(",")
print(f"Event '{event}' on {date} has {capacity} seats")

# 2. Text cleaning
dirty_text = "  Extra   SPACES and\tspecial chars!@#  "
clean = ' '.join(dirty_text.strip().split()).lower()
print(clean)  # "extra spaces and special chars!@#"

# 3. Password generator
import random
import string
password = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%', k=12))
print(f"Secure password: {password}")

# 14. Common Pitfalls
# 1. Mutable default arguments
def bad_append(item, lst=[]):  # Bad!
    lst.append(item)
    return lst

# 2. Encoding issues
# Always specify encoding when opening files
# with open('file.txt', 'r', encoding='utf-8') as f:

# 3. String vs bytes
try:
    "text" + b"bytes"  # TypeError
except TypeError:
    print("Can't mix str and bytes")


# Key Takeaways:
# 1. Use f-strings for most formatting needs (Python 3.6+)
# 2. Prefer join() for concatenating multiple strings
# 3. Remember strings are immutable - operations create new strings
# 4. Use regex for complex pattern matching
# 5. Always specify encoding when working with bytes
# 6. Leverage string methods for common operations
# 7. Use template strings for safe user-provided formatting
