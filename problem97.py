"""
Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999 and is a Mersenne prime of the form
2^6972593-1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p-1, have been
found which contain more digits.

However in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^7830457+2.

Find the last ten digits of this prime number
"""
from time import time

start = time()
x = 1
for _ in range(7830457):
    x = (2 * x) % 1000000000000
print('Answer:', (28433 * x + 1) % 10000000000)
print(time() - start)
