RANGE = 100
sum_of_squares = sum(i ** 2 for i in range(RANGE + 1))
square_of_sums = sum(range(RANGE + 1)) ** 2
print square_of_sums - sum_of_squares
