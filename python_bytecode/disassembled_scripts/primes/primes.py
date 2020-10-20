from itertools import count
from toolz import take, cons

def sieve(numbers):
    p = next(numbers)
    yield from cons(p, sieve(n for n in numbers if n % p > 0))

primes = take(10, sieve(count(2)))
for p in primes:
    print(p)
