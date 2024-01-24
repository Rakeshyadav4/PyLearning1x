# Comparison Operators:
# == Equal to
# != Not equal to
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to

x = 5
y = 10

print(x == y)  # bool -> False or false ?
print(x != y)
print(x > y)
print(y > x)
print(x <= y)
print(x >= y)

x = 5
y = 5
print( x >=y) # 5 > 5 or 5== 5 ->  True
# OR gate used in electronics
# A B O ( 0 - False, 1 - True)
#  0 0 = 0 (False and False = False)
#  0 1 = 1
#  1 0 = 1
#  1 1 = 1 (True and True = True)
'''An OR gate is a digital logic gate with two or more inputs and one output that performs logical disjunction. 
The output of an OR gate is true when one or more of its inputs are true. 
If all of an OR gate's inputs are false, then the output of the OR gate is false.'''