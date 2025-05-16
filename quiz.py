# Write a program that prompts the user for a number and prints “Fizz” if it’s divisible by 3, “Buzz” if it’s divisible by 5, “FizzBuzz” if by both, or the number otherwise.

numbers = int(input("Enter a number: "))

if numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz")
    
elif numbers % 3 == 0:
    print("Fizz")
    
elif numbers % 5 == 0:
    print("Buzz")
    
else:
    print("NONE")
    