def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

result = []
for val in fib():
    if val >= 4000000:
        break
    if val % 2 == 0:
        result.append(val)
print sum(result)
