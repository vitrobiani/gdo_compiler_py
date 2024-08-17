from functools import reduce
#Q4
def cumulative_operation(op):
    return lambda seq: reduce(op, seq)

# Factorial using the cumulative operation (multiplication)
factorial = lambda n: cumulative_operation(lambda x, y: x * y)(range(1, n + 1))

# Exponentiation using the cumulative operation (multiplication)
exponentiation = lambda base, exp: cumulative_operation(lambda x, y: x * y)([base] * exp)
print("question 4:")
print(factorial(5))
print(exponentiation(2, 3))
