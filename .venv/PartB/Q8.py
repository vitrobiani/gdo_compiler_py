# Question 8
primes_desc = lambda lst: sorted([x for x in lst if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1], reverse=True)
print("question 8:")
print(primes_desc([10, 3, 7, 11, 13, 2, 5, 4, 31, 144, 151, 191]))