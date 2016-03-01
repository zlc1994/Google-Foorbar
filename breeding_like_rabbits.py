"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But
instead of following the Fibonacci sequence like all good rabbits do, the
zombit population changes according to this bizarre formula, where R(n) is the
number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one
zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor
Boolean's minions passed the time by playing a guessing game: when will the
zombit population be equal to a certain amount? Then, some clever minion
objected that this was too easy, and proposed a slightly different game: when
is the last time that the zombit population will be equal to a certain amount?
And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you
can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation
of an integer S, returns the largest n such that R(n) = S. Return the answer as
a string in base-10 representation. If there is no such n, return "None". S
will be a positive integer no greater than 10^25.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"
"""

from functools import wraps


def memorized(f):
    """using memory to store the function return value over args."""


    cache = {}

    @wraps(f)
    def wrapped(*args):
        try:
            results = cache[args]
        except KeyError:
            results = cache[args] = f(*args)
        return results
    return wrapped


@memorized
def R(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if n%2 == 0:
            return R(n//2)+R(n//2+1)+n//2
        else:
            return R((n-1)//2-1)+R((n-1)//2)+1


def odd_binary_search(l, r, num):
    if l <= r:
        m = (l+r)//4
        if R(2*m+1) == num:
            return 2*m+1
        elif R(2*m+1) > num:
            return odd_binary_search(l, 2*m-1, num)
        elif R(2*m+1) < num:
            return odd_binary_search(2*m+3, r, num)
    else:
        return "None"


def even_binary_search(l, r, num):
    if l <= r:
        m = (l+r)//4
        if R(2*m) == num:
            return 2*m
        elif R(2*m) > num:
            return even_binary_search(l, 2*m-2, num)
        elif R(2*m) < num:
            return even_binary_search(2*m+2, r, num)
    else:
        return "None"


def result(even,odd):
    """return the str result. In fact, the int type is also accepted"""

    if even != "None" and odd != "None":
        return str(max(even,odd))
    elif even == "None" and odd != "None":
        return str(odd)
    elif even != "None" and odd == "None":
        return str(even)
    else:
        return "None"


def answer(str_S):
    """For all n>=3, the R(n) is always larger than n. So the range of our
    binary search is [0, num]. We can easily prove that R(2n) and R(2n-1) is
    monotonically increasing by induction method. Then, using binary search
    in all odd nums and even nums, return the max n if exists.
    """

    num = int(str_S)
    if num < 1:
        return "None"
    elif num in range(1,4):
        return str(num)
    else:
        if num%2 == 0:
            even = even_binary_search(4, num, num)
            odd = odd_binary_search(5, num-1, num)
        else:
            even = even_binary_search(4,num-1,num)
            odd = odd_binary_search(5,num,num)
    return result(even,odd)
