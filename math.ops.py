def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

# The code below runs *only* if you execute this file directly:
if __name__ == "__main__":
    # This allows you to test the functions by running: python math_ops.py
    print("Testing math_ops:")
    print("2 + 3 = ", add(2, 3))
    print("5 - 1 = ", subtract(5, 1))

# Every Python file has a built-in variable __name__
# If you run python math_ops.py, then __name__ == "__main__"
# If you import math_ops from another file, then __name__ == "math_ops"
