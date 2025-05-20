# 1. if Statement
age = int(input("Enter Age: "))
if age >= 18:
  print("You are an adult.")


# 2. If-else
if age >=18:
  print("You are an adult.")

else:
  print("You are Young.")


# elif Statement
score = 85
if score >= 90:
  print("Grade: A")

elif score >= 80:
  print("Grade: B")

elif score >= 70:
  print("Grade: C")

elif score >= 60:
  print("Grade: D")

else:
  print("FAIL!!")


# Nested if Statement

your_age = 24
has_license = True

if your_age >= 18:
  if has_license:
    print("You can Drive.")

  else: 
    print("You need to get a Driving Licence first.")

else:
  print("You are too Young to drive.")
