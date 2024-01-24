a = 5  # binary: 101
print(~a)
b = 10  #-6
b += 11 #(remember their will be no space between +and =)
print(b) #21
car = { "brand": "Ford","model": "Mustang","year": 1964}
car["color"]="red"
print(car)  #  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
car =	{"brand": "Ford","model": "Mustang","year": 1964}
car.pop('model')
print(car)
for x in range(6):
    print(x)
    
def print_right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
rows = int(input("Enter the number of rows for the right triangle: "))
print_right_triangle(rows)
