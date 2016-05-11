def digits(integer):
    string = str(integer)
    for i in string:
        yield int(i)


def sums(power):
    for i in range(2, sum(9**power for v in range(power))):
        total_sum = 0
        for k in digits(i):
            if total_sum > i:
                break
            total_sum += k**power
        if total_sum == i:
            yield i


def answer(power):
    print sum(sums(power))

answer(4)
answer(5)
