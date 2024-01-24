a = 5
b = 5
print(a is b) # True
print(id(a)) #140732292129704
print(id(b)) #140732292129704 = same as a and b
a = [1,2,3]
b = [1,2,3]
print (a is b) # False
print(id(a)) #3020297686976
print(id(b)) #3020299072960
#So if we are not using in list, dic, tuple then it is true or it will be false


a = 10
print(+a)
print(-a)

