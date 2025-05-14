# Loops
# 1. for loop
# Syntax:
#  for item in variable_name:
# 
fruits = ["apple", "Orange", "Mango", "Grapes"]
for fruit in fruits:
    print(fruit)  # Output: apple Orange Mango Grapes 
    print(fruits[0])  # Output: apple
    print(fruits[1])  # Output: Orange  
    print(fruits[2])  # Output: Mango
    print(fruits[3])  # Output: Grapes
    # print(fruits[4])  # Output: IndexError: list index out of range

    print(fruits[-1])  # Output: Grapes
    print(fruits[-2])  # Output: Mango

print(fruits[0:2])  # Output: ['apple', 'Orange']
print(fruits[0:3])  # Output: ['apple', 'Orange', 'Mango']

#  Using range() function
for number in range(10):
    print(number)

# 2. while loop 
# Syntax:
# while condition:
#     # code to be executed

print("While Loop")   


i=0
while i<=10:
    print(i)
    i += 1


counter = 0
while counter <4:
    print("Inside Loop")
    counter += 1

else:
    print("Inside else block")


# 3. Nested loop
colors = ["red", "blue", "orange", "yellow", "black", "white", "green"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for color in colors:
    for day in days:
        print(color, day)