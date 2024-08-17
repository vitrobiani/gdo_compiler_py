#Q2
concatenate = lambda lst: lst[0] if len(lst) == 1 else lst[0] + " " + (lambda x: x(lst[1:]))(concatenate)
print("question 2:")
print(concatenate(["This", "is", "a", "test"]))
