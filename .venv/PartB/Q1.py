from functools import reduce
#Q1
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])[:n]
print("question 1:")
print(fibonacci(13))
