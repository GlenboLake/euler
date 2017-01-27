"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def fib_with_ceiling(max_value):
    for value in fib():
        if value > max_value:
            break
        yield value

if __name__ == '__main__':
    print(sum(x for x in fib_with_ceiling(4000000) if x % 2 == 0))
