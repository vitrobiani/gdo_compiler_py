from functools import reduce
#Q2
concatenate = lambda lst: reduce(lambda x, y: x + ' ' + y, lst)
print("question 2:")
print(concatenate(["This", "is", "a", "test"]))
