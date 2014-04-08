from utils import fib

end_case = set('%d' % i for i in range(1, 10))


def is_pan_digital(slug):
    if set(slug) == end_case:
        return True
    return False

counter = 0
for val in fib(a=1, b=1):
    counter += 1
    str_val = str(val)
    if is_pan_digital(str_val[:9]) and is_pan_digital(str_val[-9:]):
        break
print counter
# Too slow
