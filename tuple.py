import itertools

# Define two tuples
tuple1 = (1, 2)
tuple2 = ('a', 'b')

# Cartesian product of tuples
product_result = tuple(itertools.product(tuple1, tuple2))

# Print result
print("Tuple Product:", product_result)
