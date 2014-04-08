def _p(m, n):
    i = 1
    while i <= m:
        j = 1
        while j <= n:
            if j >= i:
                yield i * j
            if i == 1:
                break
            j += 1
        i += 1


def P(m, n):
    distinct_terms = set()
    for val in _p(m, n):
        if val < n:
            continue
        if val not in distinct_terms:
            distinct_terms.add(val)
    print len(distinct_terms) + n - 1


P(64, 64)
P(12, 345)
# Too slow.
P(32, 10**15)
