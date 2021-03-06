"""
Primes with runs

Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by
11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

    1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated
digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are
N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only
possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

    d   M(4, d)  N(4, d)  S(4, d)
    0   2        13       67061
    1   3        9        22275
    2   3        1        2221
    3   3        12       46214
    4   3        2        8888
    5   3        1        5557
    6   3        1        6661
    7   3        9        57863
    8   3        1        8887
    9   3        7        48073

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""
from common import is_prime, miller_rabin_test

# Brute force the case in the example to make sure I get it
def n_digit_primes(n):
    for i in range(10 ** (n - 1), 10 ** n):
        if is_prime(i):
            yield i

def M(n, d):
    return max(str(num).count(str(d)) for num in n_digit_primes(n))


def N(n, d):
    nums = list(n_digit_primes(n))
    M = max(str(num).count(str(d)) for num in nums)
    return len([n for n in nums if str(n).count(str(d)) == M])


def S(n, d, nums=None):
    if nums is None:
        nums = list(n_digit_primes(n))
    M = max(str(num).count(str(d)) for num in nums)
    return sum([n for n in nums if str(n).count(str(d)) == M])

assert sum(S(4, d) for d in range(10)) == 273700

number = [0] * 10

# Shamelessly taken from mathblog.dk
def recurse(basedigit, startpos, level, fill=False):
    global number
    if level <= 0:
        if number[0] == 0:
            return 0
        n = sum(10 ** i * x for i, x in enumerate(number[::-1]))
        return n if miller_rabin_test(n) else 0
    res = 0
    if fill:
        for pos in range(len(number)):
            number[pos] = basedigit
    for pos in range(startpos, len(number)):
        for val in range(10):
            number[pos] = val
            res += recurse(basedigit, pos + 1, level - 1)
            number[pos] = basedigit
    return res


total = 0
for d in range(10):
    for i in range(1, len(number)):
        res = recurse(d, 0, i, True)
        if res:
            total += res
            break
print('Answer:', total)


# primes = list(n_digit_primes(10))
# print(len(primes), 'primes generated')
# print('Answer:', sum(S(10, d, primes) for d in range(10)))
