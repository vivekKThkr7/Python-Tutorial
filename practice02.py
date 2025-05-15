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