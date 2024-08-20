def generate_values():
 print('Generating values...')
 yield 1
 print('Generating values...')
 yield 2
 print('Generating values...')
 yield 3

def square(x):
 print(f'Squaring {x}')
 return x * x
print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)
print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)

# Output:
# Eager evaluation:
# Generating values...
# Generating values...
# Generating values...
# Squaring 1
# Squaring 2
# Squaring 3
# [1, 4, 9]

# Lazy evaluation:
# Generating values...
# Squaring 1
# Generating values...
# Squaring 2
# Generating values...
# Squaring 3
# [1, 4, 9]

# Lazy evaluation in the context of this program demonstrates how Python can defer computations until they are necessary, particularly using generators.
# This approach can save resources and improve efficiency by avoiding unnecessary calculations and memory usage.
# The key differences:
# Lazy evaluation minimizes memory usage because it processes values one at a time,
# whereas eager evaluation consumes all values at once and stores them in memory.
# In addition, in lazy evaluation, the processing is deferred and can be more efficient if not all values are needed.
# With eager evaluation, all values are generated and processed upfront.
