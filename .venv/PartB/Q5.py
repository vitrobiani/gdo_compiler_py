from functools import reduce
# Question 5
sum_squared = lambda lst: reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst)))
print("question 5:")
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_squared(lst))
