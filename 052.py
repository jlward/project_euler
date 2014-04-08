def is_valid(value):
    x1 = sorted(list(str(value)))
    x2 = sorted(list(str(value * 2)))
    if (x1 != x2) or (len(x1) != len(x2)):
        return False
    x3 = sorted(list(str(value * 3)))
    if (x1 != x3) or (len(x1) != len(x3)):
        return False
    x4 = sorted(list(str(value * 4)))
    if (x1 != x4) or (len(x1) != len(x4)):
        return False
    x5 = sorted(list(str(value * 5)))
    if (x1 != x5) or (len(x1) != len(x5)):
        return False
    x6 = sorted(list(str(value * 6)))
    if (x1 != x6) or (len(x1) != len(x6)):
        return False
    return True


value = 1
while True:
    if is_valid(value):
        break
    value += 1

print value
