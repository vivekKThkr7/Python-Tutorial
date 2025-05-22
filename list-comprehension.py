
# List Comprehension in Python

# Example 1: Create list of squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Equivalent for loop:
# squares = []
# for x in range(5):
#     squares.append(x**2)

# Example 2: Convert strings to uppercase
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# 2. Conditional Filtering (if clause)

# Example 1: Even numbers filter
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Example 2: Filter words longer than 5 characters
words = ['python', 'is', 'awesome', '!']
long_words = [word for word in words if len(word) > 2]
print(long_words)  # Output: ['python', 'awesome']

# 3. Conditional Expressions (if-else)


# Example 1: Even-Odd classifier
even_odd = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]
print(even_odd)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# Example 2: Square even numbers, cube odd numbers
numbers = [x**2 if x % 2 == 0 else x**3 for x in range(7)]
print(numbers)  # Output: [0, 1, 4, 27, 16, 125, 36]

# 4. Nested Loops

# Example 1: Matrix flattening
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2: All possible pairs
colors = ['red', 'green']
sizes = ['S', 'M']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)  # Output: [('red', 'S'), ('red', 'M'), ('green', 'S'), ('green', 'M')]

# 5. Multiple Variables

# Example: Using zip() with multiple iterables
names = ['Alice', 'Bob']
scores = [85, 92]
name_scores = [f'{name}: {score}' for name, score in zip(names, scores)]
print(name_scores)  # Output: ['Alice: 85', 'Bob: 92']

# Example: Using enumerate() for index-value pairs
letters = ['a', 'b', 'c']
indexed = [f'{i}: {letter}' for i, letter in enumerate(letters)]
print(indexed)  # Output: ['0: a', '1: b', '2: c']

# 6. Nested List Comprehensions

# Example 1: Create 2D matrix
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Example 2: Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# 7. Advanced Concepts

# Example 1: Using functions in comprehensions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(20) if is_prime(x)]
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Example 2: Multiple conditions
numbers = [x for x in range(20) if x % 2 == 0 if x % 5 == 0]
print(numbers)  # Output: [0, 10]

# Example 3: Dictionary comprehension (related concept)
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example 4: Set comprehension (related concept)
unique_lengths = {len(word) for word in ['hello', 'world', 'python']}
print(unique_lengths)  # Output: {5, 6}


# 8. Performance Considerations

# List comprehensions are generally faster than equivalent for-loops
# but avoid overly complex comprehensions for better readability

# example:
results = [x**2 for x in range(1000) if x % 3 == 0]

# Bad example (hard to read):
# complex = [x**2 if x%2==0 else x**3 for x in [y+1 for y in range(100)] if x > 10]

# 9. When to Avoid List Comprehensions

# - When side effects are needed
# - When complex error handling is required
# - When the logic becomes too nested/complex

# Instead of:
# result = []
# for x in data:
#     try:
#         result.append(process(x))
#     except Exception:
#         result.append(None)

# Prefer using explicit loops for complex error handling


# Final Notes:
# - List comprehensions are powerful but should prioritize readability
# - Can often replace map()/filter() combinations
# - Remember that comprehensions create new lists (memory considerations)
