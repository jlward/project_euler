def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

counter = 0
for val in fib():
    if val >= len(str(val)) >= 1000:
        break
    counter += 1
print counter
