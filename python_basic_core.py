#Basic if-elif-lese structure

age = 25
print("----Basic Conditionals----")
if age < 18:
  print("Minor")

elif 18 <= age < 65:
  print("Adult")

else:
  print("Senior")

# Ternary Operator
status = "Eligible" if age >= 18 else "Not Eligible"
print(f"Voting Status: {status}")

# Chained Comparisions
temperature = 22 
if 20 <= temperature <= 25:
  print("Comfortable temperature")
  

# Truth Value Comparisions
name = " "
if not name:
    print("Name is empty")
    
    
    
# For Loops Basics
print("---For Loops---")
print("List Iteration: ")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruits}")
    
print("Range Function: ")
for i in range(3):
    print(i)
    
# While Loops
count = 3
while count > 0:
    print(f"countdown: {count}")
    count -= 1
    
# Loop Control Statements
for num in range(10):
    if num == 3:
        continue
    if num == 7:
        break
    print(num)
    
    
# Advanced Looping 
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruits}")
    
    
# Zip for parellel Iteration
colors = ['red', 'yellow', 'purple']
for fruits, color in zip (fruits, colors):
    print(f"{fruits} is {color}")
    
# List Comparisions (Advanced)
squares = [x**2 for x in range(1, 6)]
print(f"squares: {squares}")
