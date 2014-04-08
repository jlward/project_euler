from utils import fib

counter = 0
for val in fib():
    if val >= len(str(val)) >= 1000:
        break
    counter += 1
print counter
