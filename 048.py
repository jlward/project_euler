def answer(max_value):
    total = 0
    for i in range(1, max_value):
        total += i**i
    print str(total)[-10:]


answer(1000)
