numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# num%2==0
# even_numbers = [2, 4, 6, 8, 10]


# filter -> Number element can be less or equal the list
# filter condition should be true or false condition
# map executes on every element but filter filters it and hence it gives = or fewer elements.
def is_even(num):
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
# print(even_numbers)  It will give output as <filter object at 0x000001F7946ABA60> so covert it into list
even_numbers_list = list(even_numbers)
print(even_numbers_list)  # [2, 4, 6, 8, 10]
