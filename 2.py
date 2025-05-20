# 1. Arithmetic Operators
print("\n1. Arithmetic Operators")
a = 10
b = 3

addition = a + b
subtraction = a - b
product = a * b
quotent = a / b
modulus = a % b
exponentiation = a**b
print(
    f"{addition}, {subtraction}, {product}, {quotent}, {modulus}, {exponentiation}"
)

# 2. Comparison Operators
print("\n2. Comparison Operators")
c = 22
d = 44
print(c == d)
print(c != d)
print(c < d)
print(c > d)
print(c < d)
print(c > d)
print(c == d)

# 3. Logical Operators
print("\n3. Logical Operators")
x = True
y = False

and_result = x and y
or_result = x or y
not_result = not x
print(and_result, or_result, not_result)


# 4. Assignment Operators
print("\n4. Assignment Operators")
m = 10
n = 5
m += n
print(m)
m -= n
print(m)
m *= n
print(m)
m /= n
print(m)
m %= n
print(m)
m //= n
print(m)



# 5. Identity Operators
print("\n5. Identity Operators")
numbers = [1, 2, 3]
numbers2 = numbers
numbers3 = numbers.copy()
print(numbers is numbers2)
print(numbers is numbers3)  
print(numbers is not numbers3)


# Display the output in different ways
print("Hello World!")
name = "Vivek Thakur"
age = 25
print("Name: ", name, "Age: ", age)
print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format(name, age))
