# String = bunch of character
# #name="rakesh"
# age=33
# f-strings
#print(f"My name is {name} and I am {age} years old")
#str.format
#print("My name is {} and I am {} years old.".format(name,age)

c = 'A'
print(c)
name = "rakesh"
print(name)
my_line = 'this is "code"'
print(my_line)

Default = "PO"
count = 0  # Initialize a counter variable
for i in range(56001, 57099):
    print(f'{Default}{i}')
    count += 1  # Increment the counter for each iteration

print("Number of items in the output:", count)  # Print the count


base_string = "PO"
start_number = 56001
end_number = 57099
count = 0
for i in range(start_number, end_number+1):
    print(f'{base_string}{i}')
    count += 1
print("Number of items in the output:", count)