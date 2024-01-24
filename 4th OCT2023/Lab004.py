print('Hello World')
print('Rakesh', 'Yadav', 'Lucky')  # *args multiple number of arguments you can enter
print('Rakesh', 'Yadav', 'Lucky', sep='*')  # sep separate the arguments by given value(*)
#print('Rakesh', 'Yadav', 'Lucky', end='\t')  # sep separate the arguments by given value(*)
print('Rakesh', 'Yadav', 'Lucky', sep='*', end='\t')  # \t give tab space at the end
print('Lucky')
print('Lucky')
print('Lucky')

# ESCAPE SEQUENCE
#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value
'''print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

*objects: This argument represents a variable number of objects to be printed. 
You can pass any number of objects separated by commas. 
These objects will be converted to strings using the str() function before being printed.

sep: This is an optional argument that specifies the string that separates multiple objects when printed. 
The default separator is a space ' '.

end: This is an optional argument that specifies the string that is printed at the end of the line. 
The default value is a newline character '\n', which causes the output to move to the next line after printing.
'''