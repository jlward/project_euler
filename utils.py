def fib(a=0, b=1):
    while 1:
        yield a
        a, b = b, a + b
