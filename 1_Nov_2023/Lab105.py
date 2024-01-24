words = ["apple", "banana", "cherry", "datting", "elderberry", "fig"]
min_len = 6

# we are defining condition
def check_len(aboveword):
    return len(aboveword) > min_len
# we can't call function in the output, so we're telling that answer should use the function along with given values from list

answer = list(filter(check_len,words))
# or we can convert it as list later as (list_answer = answer and then print list_answer)
print(answer)