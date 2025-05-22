# Advanced List Comprehension Concepts: 

# 10. Walrus Operator (Python 3.8+)

# Assign and use variables within comprehensions using :=
# Syntax: [expression with assignment for item in iterable if condition]

# Example: Read file and check lengths while processing
lines = ["Hello", "Python", "Programming", "List", "Comprehensions"]
long_words = [(word, length) for line in lines if (length := len(line)) > 5]
print(long_words)  # Output: [('Python', 6), ('Programming', 11), ('Comprehensions', 14)]


# 11. Nested Comprehensions with Multiple Levels

# Example: 3D matrix creation
matrix_3d = [[[i+j+k for k in range(2)] for j in range(3)] for i in range(4)]
print(matrix_3d)
# Output: [[[0, 1], [1, 2], [2, 3]], 
#         [[1, 2], [2, 3], [3, 4]], 
#         [[2, 3], [3, 4], [4, 5]], 
#         [[3, 4], [4, 5], [5, 6]]]

# Example: Flatten 3D matrix
flat_3d = [num for cube in matrix_3d 
           for layer in cube 
           for num in layer]
print(flat_3d)  # Output: [0, 1, 1, 2, 2, 3, 1, 2, 2, 3, 3, 4, ...]


# 12. Generator Expressions vs List Comprehensions

# Use () instead of [] for lazy evaluation
gen_exp = (x**2 for x in range(1000000))  # Memory efficient
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1


# 13. Exception Handling in Comprehensions

# Example: Safe conversion using helper function
def safe_convert(x):
    try:
        return int(x)
    except ValueError:
        return None

values = ['12', '3.14', '45', 'text']
converted = [safe_convert(x) for x in values]
print(converted)  # Output: [12, None, 45, None]


# 14. Combining with itertools

import itertools

# Example: Cartesian product using itertools.product
colors = ['red', 'blue']
sizes = ['S', 'L']
combos = [(c, s) for c, s in itertools.product(colors, sizes)]
print(combos)  # Output: [('red', 'S'), ('red', 'L'), ('blue', 'S'), ('blue', 'L')]


# 15. Memory Considerations

# For large datasets, consider generator expressions
# Bad practice for huge data: [x**2 for x in range(10**8)]  # Allocates massive list
# Better: (x**2 for x in range(10**8))  # Generates values on demand


# 16. Functional Programming Patterns

# Example: Combining with map and filter
data = [1, 2, 3, 4, 5]
processed = [y for y in map(lambda x: x*2, filter(lambda x: x%2 ==0, data))]
print(processed)  # Output: [4, 8]

# Equivalent comprehension:
processed = [x*2 for x in data if x%2 ==0]
print(processed)  # Output: [4, 8]


# 17. Recursive Comprehensions

# Not recommended, but possible using nested functions
def recursive_comp(n):
    return [i*2 for i in (recursive_comp(n-1) if n > 1 else [1])]

print(recursive_comp(3))  # Output: [8]


# 18. Advanced Filter Patterns

# Example: Multiple condition filtering with different actions
numbers = range(20)
result = [
    "FizzBuzz" if x%15 ==0 else
    "Fizz" if x%3 ==0 else
    "Buzz" if x%5 ==0 else x
    for x in numbers
]
print(result[:15])
# Output: ["FizzBuzz", 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14]


# 19. Nested Conditional Logic

# Example: Complex eligibility check
users = [
    {'name': 'Alice', 'age': 25, 'status': 'active'},
    {'name': 'Bob', 'age': 17, 'status': 'inactive'},
    {'name': 'Charlie', 'age': 30, 'status': 'active'}
]

eligible = [user['name'] for user in users 
           if user['status'] == 'active' 
           and (user['age'] >= 18 or user['age'] >= 16 and user['age'] < 18)]
print(eligible)  # Output: ['Alice', 'Charlie']


# 20. Performance Optimization

# Demonstrate time difference with large datasets
import timeit

# List comprehension
lc_time = timeit.timeit('[x**2 for x in range(1000000)]', number=10)
print(f"List comp time: {lc_time:.4f}s")

# Equivalent loop
loop_time = timeit.timeit('''
result = []
for x in range(1000000):
    result.append(x**2)
''', number=10)
print(f"Loop time: {loop_time:.4f}s")

# Typical output:
# List comp time: 0.8500s
# Loop time: 1.2000s

# 21. Anti-Patterns and Common Mistakes

# 1. Modifying variables used in comprehension
x = 5
bad_example = [x for x in range(3)]  # Overwrites x!
print(x)  # Output: 2 (Python 3.x behavior)

# 2. Ignoring None values properly
data = [1, None, 2, None, 3]
clean_data = [x for x in data if x is not None]
print(clean_data)  # Output: [1, 2, 3]

# 3. Avoiding side effects
# Bad: [print(x) for x in range(3)]  # Creates unnecessary list
# Good: for x in range(3): print(x)


# 22. Real-World Data Processing Example

# Process CSV data (simulated)
csv_data = [
    "Alice,25,Engineer",
    "Bob,32,Designer",
    "Charlie,19,Intern"
]

processed = [
    {
        'name': parts[0],
        'age': int(parts[1]),
        'role': parts[2],
        'status': 'Senior' if int(parts[1]) > 30 else 'Junior'
    }
    for line in csv_data
    if (parts := line.split(',')) and len(parts) == 3
]

print(processed)
# Output: [
#   {'name': 'Alice', 'age': 25, 'role': 'Engineer', 'status': 'Junior'},
#   {'name': 'Bob', 'age': 32, 'role': 'Designer', 'status': 'Senior'},
#   {'name': 'Charlie', 'age': 19, 'role': 'Intern', 'status': 'Junior'}
# ]


# Key Advanced Takeaways:
# 1. Use walrus operator for combined assignment/condition checks
# 2. Generator expressions for memory efficiency
# 3. Combine comprehensions with itertools for complex iterations
# 4. Handle exceptions through wrapper functions
# 5. Be mindful of variable scope and side effects
# 6. Use comprehensions for data transformation pipelines
# 7. Consider readability vs performance trade-offs
