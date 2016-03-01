"""
Line up the captives
====================

As you ponder sneaky strategies for assisting with the great rabbit escape, you
realize that you have an opportunity to fool Professor Booleans guards into
thinking there are fewer rabbits total than there actually are.

By cleverly lining up the rabbits of different heights, you can obscure the
sudden departure of some of the captives.

Beta Rabbits statisticians have asked you for some numerical analysis of how
this could be done so that they can explore the best options.

Luckily, every rabbit has a slightly different height, and the guards are lazy
and few in number. Only one guard is stationed at each end of the rabbit
line-up as they survey their captive population. With a bit of misinformation
added to the facility roster, you can make the guards think there are different
numbers of rabbits in holding.

To help plan this caper you need to calculate how many ways the rabbits can be
lined up such that a viewer on one end sees x rabbits, and a viewer on the
other end sees y rabbits, because some taller rabbits block the view of the
shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm, 50
cm, 40 cm, and then 20 cm, a guard looking from the left side would see 2
rabbits (30 and 50 cm) while a guard looking from the right side would see 3
rabbits (20, 40 and 50 cm). 

Write a method answer(x,y,n) which returns the number of possible ways to
arrange n rabbits of unique heights along an east to west line, so that only x
are visible from the west, and only y are visible from the east. The return
value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1 and as
large as the total number of rabbits (n).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Output:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Output:
    (string) "24"

"""


from math import factorial
from functools import wraps


def memorized(f):
    """using memory to store the function return value over args."""
    cache = {}

    @wraps(f)
    def wrap(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrap


@memorized
def combination(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k)) if n >= k else 0



@memorized
def permutation(n, k):
    """return the amount of combiantions that k rabbits can be seen over n 
    rabbits at the front.
    """

    
    #There is no such case
    if k > n:
        return 0


    #only one case, order the rabbits from short to tall
    elif k == n:
        return 1


    #all the n-1 rabbits is behind the tallest one, is all the permutations
    #of the n-1 rabbits
    elif k == 1:
        return factorial(n-1)


    #only one rabbits is invisible, if is the shortest one, place it behind
    #any n-1 rabbits. If is the second shortest one, is n-2.
    #so the total is sum(range(n)) = n*(n-1)/2
    elif k == n-1:
        return sum(range(n))


    #1. If the shortest is visible, must in the front. k-1 rabbits can be 
    #seen over the n-1.
    #2. If the shortest is invisible, it will have n-1 choice to place 
    #behind any k rabbits can be seen over n-1 rabbits.
    else:
        return permutation(n-1, k-1)+permutation(n-1, k)*(n-1)


def answer(x, y, n):
    """
    total visible : x+y-2
    left visible :x-1
    right visible:y-1
    choose x-1 from x+y-2 is combination(x+y-2,x-1)

    the tallest is always visible.
    Consider the n-1 rabbits except the tallest.
    let x-1+y-1 rabbits can be seen over these n-1 rabbits, then place the 
    tallest one into the n-1 rabbits such that it's left having x-1 rabbits 
    while right y-1 rabbits. Thus, x is visiable from left and y is visible
    from the right.
    """


    return permutation(n-1,x+y-2)*combination(x+y-2,x-1)
