"""
Undercover underground
======================

As you help the rabbits establish more and more resistance groups to fight
against Professor Boolean, you need a way to pass messages back and forth.

Luckily there are abandoned tunnels between the warrens of the rabbits, and you
need to find the best way to use them. In some cases, Beta Rabbit wants a high
level of interconnectedness, especially when the groups show their loyalty and
worthiness. In other scenarios the groups should be less intertwined, in case
any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow, and no two
warrens should ever have more than one tunnel between them. Your assignment:
count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three
distinct ways to connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect each
warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect N
distinctly labelled warrens with exactly K tunnels, so that there is a path
between any two warrens. 

The return value must be a string representation of the total number of ways to
do so, in base 10.
N will be at least 2 and at most 20. 
K will be at least one less than N and at most (N * (N - 1)) / 2

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) N = 2
    (int) K = 1
Output:
    (string) "1"

Inputs:
    (int) N = 4
    (int) K = 3
Output:
    (string) "16"

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
    return factorial(n)/(factorial(k)*factorial(n-k)) if n>=k else 0

@memorized
def answer(N, K):
    """The answer is the amount of labelled connencted graphs over K edges 
    and N nodes. Here is the formula(http://math.stackexchange.com/a/690422)  
    $$
    q_{n, k} =
    \begin{cases}
    0 \quad\text{if}\quad k\lt n-1 \quad\text{or}\quad k\gt n(n-1)/2 \\
    n^{n-2} \quad\text{if}\quad k = n-1, 
    \quad\text{and otherwise}\\
    {n(n-1)/2\choose k}
    - \sum_{m=0}^{n-2} {n-1\choose m} 
    \sum_{p=0}^k {(n-1-m)(n-2-m)/2 \choose p} q_{m+1, k-p}. 
    \end{cases}
    $$
    """


    if K < N-1 or K > combination(N, 2):
        return 0


    #Cayley's Formula
    elif K == N-1:
        return int(N**(N-2))

    else:
        result = combination(N*(N-1)/2, K)
        for m in range(N-1):
            temp = 0
            for p in range(K+1):
                temp += combination((N-1-m)*(N-2-m)/2, p)*answer(m+1, K-p)
            result -= combination(N-1, m)*temp
        return result

