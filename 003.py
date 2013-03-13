num = 600851475143
counter = 2
primes = []

while num:
    if num == 1:
        break
    if num % counter == 0:
        primes.append(counter)
        num = num / counter
        counter = 2
    else:
        counter += 1
print max(primes)
