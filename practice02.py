# Print your Name
print("The name is Vivek Kumar Thakur.")

# 2. Arithmentic Operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"The sum of {num1} and {num2} is {num1 + num2}")
print(f"The difference from {num2} to {num1} is {num2 - num1}")
print(f"The Product of {num1} and {num2} is {num1 * num2}")
print(f"The Quotent of {num1} from {num2} is {num1 / num2}")
print(f"The remainder from {num1} to {num2} is {num1 % num2}")


# 3. Check Even/odd
number = int(input("Enter any whole number: "))
if number % 2 == 0:
    print(f"{number} is even number.")
    
else:
    print(f"{number} is odd number.")
    
# alternative
print("Even" if number % 2 == 0 else "Odd")


# 4. Factorial of a number
n = int(input("Enter a number whose Factorial is need to be calculated: "))
factorial = 1
for i in range (1, n+1):
    factorial*= i
print(f"Factorial of {n} is {factorial}")

# 5. Fibonacci Sequence
num3 = 10
a, b = 0, 1 
for _ in range(num3):
    print(a, end=" ")
    a, b = b, a + b
    
    
# 6. Check Prime number
num = 29
is_prime = True 
for i in range(2, int(num**0.5) +1):
    if num % i == 0:
        is_prime = False
        break
    print("Prime " if is_prime else "Not Prime")
    

# 7. Reverse a string 
name1 = "Vivek"
print(name1[::-1])


# 8. Palindrome Check
s = "Hello"
print("Palindrome" if s == s[:: -1] else "Not Palindrome")

word = "madam"
print(f"{word} {'is a Palindrome' if word == word[:: -1] else 'is Not a Palindrome'}")



# 9. Largest Element in a List 
numbers = [1,3,5,7,9,11,13,15]
print(max(numbers))
print(type(max(numbers)))
# sum of List of elements
print(sum(numbers))


# 10. Remove Duplicate form List
sets = [1,2,3,2,3,5,6,7]
unique = []
for num in sets:
    if num not in unique:
        unique.append(num)
print(unique)


# 11. Celcius to Fahrenheit calculations
c = 37.5 
f = (c * 9/ 5) + 32 
print(f"{c} degree is equals to {f} degree of temperature")



# 12. List Compprehension (Squares)
squares = [x**2 for x in range(1, 10)]
print(squares)


# 13. Swapping Variables
a = 15
b = 10
a, b = b, a 
print(f"a = {a}, b = {b}")

name01 = "Vivek"
name02 = "Thakur"
name01, name02 = name02, name01
print(f"the name is {name01} {name02}.")



# 14. Multiplication Table
n = 2
for i in range (1, 11):
    print(f"{n} * {i} = {n*i}")
    
n2 = 3
for i in range(1, 11):
    print(f"{n2} * {i} = {n*i}")
    

# 15. Find GCD/HCF
import math
print(f'GCD = {math.gcd(2, 4)}')


# 16. Current Date and Time 
import datetime
print(datetime.datetime.now())