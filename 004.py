import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).

    http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


def products():
    for i in range(100, 1000):
        for j in range(100, 1000):
            yield i * j


@memoized
def is_palindrome(val):
    '''
    >>> is_palindrome(10)
    False
    >>> is_palindrome(11)
    True
    '''
    base = list(str(val))
    return base == list(reversed(base))


results = []
for i in products():
    if is_palindrome(i):
        results.append(i)
print max(results)
