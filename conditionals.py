# Conditionals: 


# 1. if statement
a= 10
b=5
if a>b:
    print("a is greater than b")



# 2. if-else statements
if a>b:
    print("a is greater than b.")

else:
    print("b is greater than a.")



# 3. if-elif-else statements
num1= 10
num2= 20
if num1>num2:
    print("num1 is greater.")

elif num1<num2:
    print("num2 is greater.")

else:
    print("num1 is equals to num2.")


# 4. Nested if statements
marks= 85
if marks>= 60:
    print("You are pass.")
    if marks>= 80:
        print("You are in distinction.")
    else:
        print("You are in first division.")
else:
    print("You are fail.")
    