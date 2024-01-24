# keywords and Identifiers
import keyword
print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif','else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 '''
'''Rules for writing identifiers:
Identifiers can be a combination of letters in 
lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
An identifier cannot start with a digit.
Keywords cannot be used as identifiers.
We cannot use special symbols like !, @, #, $, %, etc. in our identifier.
An identifier can be of any length.
Examples of valid identifiers: myVar, var1, _var, _1_var
Examples of invalid identifiers: 1var, my-var, my@, my var, break
'''




a = input("enter you name\n")  # escape function \n used to input the name in the next line
print(a)
a = input('enter your first name\n')
b = input ('enter your last name\n')
print (b,a,sep='-',end='\t\n')
name = input('enter your name\n')
print('you are welcome',name)

