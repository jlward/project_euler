from utils import fib

result = []
for val in fib():
    if val >= 4000000:
        break
    if val % 2 == 0:
        result.append(val)
print sum(result)
