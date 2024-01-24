'''Write a Python program to calculate the area of a circle given its radius using the formula
area=π×r^2 ( Take pie as 3.14)'''
# Taking pi as 3.14
pi = 3.14
# input radius
radius = float(input("Enter the radius of the circle:\n "))
# Calculate the area of the circle
area = pi * radius ** 2
# Display the area of the circle
print(f"The area of the circle with radius {radius} is {area}")

'''Create a program that takes two numbers as input and prints whether 
the first number is greater than, less than, or equal to the second number.'''
# Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Compare the two numbers and print the result
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

'''Use the ternary operator to find the maximum of three numbers entered by the user.'''
# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Use the ternary operator to find the maximum
max_number = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
# Display the maximum number
print(f"The maximum of {num1}, {num2}, and {num3} is {max_number}")

'''Develop a Python script that calculates the square and cube of a given number.'''
# Get the number from the user
number = float(input("Enter a number: "))
# Calculate the square and cube of the number
square = number ** 2
cube = number ** 3
# Display the square and cube of the number
print(f"The square of {number} is {square}")
print(f"The cube of {number} is {cube}")

