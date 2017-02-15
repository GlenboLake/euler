"""
Cube digit pairs

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By
placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers. In fact, by
carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred:
01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the
other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
{0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be
impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""
# Since 6 and 9 are the same, treat all 9s and 6s, requiring 01, 04, 06, 16, 25, 36, 46, 64, and 81. This makes 46 and
# 64 duplicates. All the pairs needed, sorted, are:
from itertools import combinations

pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (1, 8), (2, 5), (3, 6), (4, 6)]


def check_for_pair(pair, dice):
    return pair[0] in dice[0] and pair[1] in dice[1] or pair[1] in dice[0] and pair[0] in dice[1]


possible_dice = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))
count = 0
for dice in combinations(possible_dice, 2):
    if all(check_for_pair(pair, dice) for pair in pairs):
        count += 1
print(count)
