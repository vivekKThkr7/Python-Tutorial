#  Variable and Data Types

# # A variable is a container for storing data values.
### Python me vairiable ko declare karne ke liye koi ek keyword rakhna parta hai. eg: age = 20, here age is a variable and 20 is a value.

## Data Types
# Variables mai j data store hota hai uska ek type hota hai. 
### int, float, str, bool
# int: Integer, whole number
# float: Decimal number
# str: String, text
# bool: Boolean, True or False
# 

# Exapmple:
age = 25  # int   (Here age is a variable and 25 is a value)
name = "John Doe"  # str
is_student = True  # bool
height = 5.9    # float
letter = 'A' # str

print(age) # Output: 25
print(name) # Output: John Doe
print(is_student) # Output: True
print(height) # Output: 5.9 
print(letter) # Output: A

# to check the type of a variable, we can use the type() function
print(type(age))
print(type(name))





# Operators
# Operators are used to perform operations (add, sub, divide, etc.)on variables and values.

# 1. Arithmetic Operators
# +, -, *, /, %, **, //

num1 = 10
num2 = 3
print(num1 + num2) # Output: 13
print(num1 - num2) # Output: 7
print(num1 * num2) # Output: 30
print(num1 / num2) # Output: 3.3333333333333335
print(num1 % num2) # Output: 1
print(num1 ** num2) # Output: 1000
print(num1 // num2) # Output: 3


# # 2. Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=
num = 10
num += 5 # num = num + 5
print(num) # Output: 15

num -= 5 # num = num - 5
print(num) # Output: 10

num *= 5 # num = num * 5
print(num) # Output: 50

num /= 5 # num = num / 5
print(num) # Output: 10.0

num %= 5 # num = num % 5
print(num) # Output: 0.0

num **= 5 # num = num ** 5
print(num) # Output: 0.0

num //= 5 # num = num // 5
print(num) # Output: 0.0

# # 3. Comparison Operators
# ==, !=, >, <, >=, <=
num3 = 10
num4 = 20
print(num3 == num4) # Output: False
print(num3 != num4) # Output: True
print(num3 > num4) # Output: False
print(num3 < num4) # Output: True
print(num3 >= num4) # Output: False
print(num3 <= num4) # Output: True


# # 4. Logical Operators
# and, or, not
num5 = True
num6 = False
print(num5 and num6) # Output: False
print(num5 or num6) # Output: True
print(not num5) # Output: False


# # 5. Identity Operators
# is, is not
num7 = [1, 2, 3]
num8 = [1, 2, 3]
print(num7 is num8) # Output: False
print(num7 is not num8) # Output: True

