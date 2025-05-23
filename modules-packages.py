
# Section 1: Writing a Simple Module

# A module is any .py file with code you want to reuse.
# Here is an example module code. Imagine this part is in math_ops.py:

def add(a, b):
    """
    add(a, b) -> number
    Return the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    subtract(a, b) -> number
    Return a minus b.
    """
    return a - b

# When this file runs directly, __name__ == "__main__"
# That means we can test our module functions here:
if __name__ == "__main__":
    print("Testing math_ops functions:")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print()


# Section 2: Importing Modules

# In another file (main.py), you can import and use math_ops:
#
# import math_ops           # import whole module
# from math_ops import add  # import only add()
# import math_ops as mo     # import with alias 'mo'
#
# Then in code:
#    result1 = math_ops.add(10, 5)
#    result2 = add(10, 5)
#    result3 = mo.subtract(10, 5)
#
# And use if __name__ == "__main__": to run main() only when executed directly.


# Section 3: The __name__ Variable

# Every Python file has __name__. When you run "python file.py", __name__ == "__main__".
# When you import that file, __name__ == module name (e.g., "math_ops").
# Use this to separate runnable tests from importable code.


# Section 4: What Is a Package?

# A package is a folder with an __init__.py file.
# It groups related modules together.
#
# Structure:
# mypackage/               [folder name is the package name]
#   __init__.py           [required to make Python treat folder as package]
#   greetings.py          [module 1]
#   farewells.py          [module 2]

# File: greetings.py (inside mypackage)
def say_hello(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

# File: farewells.py (inside mypackage)
def say_goodbye(name):
    """Return a friendly farewell."""
    return f"Goodbye, {name}!"

# File: __init__.py (inside mypackage)
# Here we import functions to make them available directly on package:
# from .greetings import say_hello
# from .farewells import say_goodbye


# import mypackage
# mypackage.say_hello("Vivek")
# mypackage.say_goodbye("Mr. X")


# Section 5: Packaging for Distribution

# To let others install your package with pip, create setup.py:
#
# from setuptools import setup, find_packages
#
# setup(
#     name="mypackage",
#     version="0.1.0",
#     packages=find_packages(),
#     author="Your Name",
#     description="A simple greeting package",
# )
#
# Then run: pip install -e .
# Now any script on your computer can import mypackage.
