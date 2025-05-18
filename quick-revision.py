# Prompt the user to enter numbers and convert the input to integers. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print(f"The sum of {num1} and {num2} is {sum}")

num3 = float(input("Enter 3rd number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is Largest.")
    
elif num2 > num1 and num2 > num3:
    print(f"{num2} is Largest.")
    
else:
    print(f"{num3} is Largest.")


number = int(input("Enter any whole number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
    
elif number % 2 != 0:
    print(f"{number} is Odd number.")
    
else:
    print(f"{number} is zero.")
    
    
    
   
#Multiplication Table   
n = int(input("Enter Number: ")) 
for i in range (1, 11):
    product = n * i
    print(f"{n} * {i} = {product}")
    
    
    

    
