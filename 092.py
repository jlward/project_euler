def numbers(val):
    for digit in str(val):
        yield int(digit)


def answer():
    in_1 = set()
    in_89 = set()

    def get_next_value(val):
        return sum(v**2 for v in numbers(val))

    def goes_to_1(val):
        if val == 1:
            return True
        if val == 89:
            return False
        if val in in_1:
            return True
        if val in in_89:
            return False
        next_val = get_next_value(val)
        if next_val in in_1:
            return True
        if next_val in in_89:
            return False
        while 1:
            if next_val in in_1:
                return True
            if next_val in in_89:
                return False
            if next_val == 1:
                return True
            if next_val == 89:
                return False
            next_val = get_next_value(next_val)
        if next_val == 1:
            return True
        if next_val == 89:
            return False

    def get_nums(val):
        yield val
        next_val = get_next_value(val)
        yield next_val
        while 1:
            if next_val in in_1:
                break
            if next_val in in_89:
                break
            if next_val == 1:
                break
            if next_val == 89:
                break
            next_val = get_next_value(next_val)
            yield next_val
        yield next_val

    for i in xrange(1, 10000001):
        if goes_to_1(i):
            for val in get_nums(i):
                in_1.add(val)
        else:
            for val in get_nums(i):
                in_89.add(val)
    print len(in_89)


# TODO this is a little slow for me. I could only do the loops once if I used
# recursion.
answer()
