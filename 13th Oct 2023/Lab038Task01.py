'''Task #1
Explain the difference between the = operator and the == operator in Python.
What does the ** operator do in Python, and how is it used?
What does the ^ operator do in Python, and in what context is it commonly used?'''
'''Difference between the = operator and the == operator:
The = operator is used for variable assignment. It assigns the value on the right to the variable on the left.'''
x = 5  # Assigns the value 5 to the variable x

'''The == operator is used for equality comparison. 
It checks if the values on the left and right are equal and 
returns a boolean value, either True or False, based on the comparison.'''
x = 5
y = 5
print(x == y)  # Checks if x is equal to y, which evaluates to True

'''The ** operator in Python:
The ** operator is used for exponentiation. It raises the number on the left to the power of the number on the right.'''
x = 2
y = 3
print(x ** y)  # Computes 2 to the power of 3, which evaluates to 8

'''The ^ operator in Python:
The ^ operator is the bitwise XOR (exclusive OR) operator in Python. 
It performs the XOR operation on the binary representations of the numbers.'''
x = 5  # Binary representation 101
y = 3  # Binary representation 011
print(x ^ y)  # Performs the XOR operation: 101 ^ 011 = 110, which evaluates to 6 in decimal format
x = 5  # Binary representation 101
y = 3  # Binary representation 011
print(x ^ y)  # Performs the XOR operation: 101 ^ 011 = 110, which evaluates to 6 in decimal format
