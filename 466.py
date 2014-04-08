def _p(m, n):
    i = 1
    while i <= m:
        j = 1
        while j <= n:
            yield i * j
            j += 1
        i += 1


def P(m, n):
    distinct_terms = set()
    for val in _p(m, n):
        if val not in distinct_terms:
            distinct_terms.add(val)
    print len(distinct_terms)


P(64, 64)
P(12, 345)
# Too slow.
P(32, 10**15)
