"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid
laboratory, you had to develop a system to track them, since some habitually
continue to gnaw on the heads of their brethren and need extra supervision. For
obvious reasons, you based your rabbit survivor tracking system on a binary
search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and
each, luckily enough, had a distinct age. For a given group, the first rabbit
became the root, and then the next one (taken in order of rescue) was added,
older ages to the left and younger to the right. The order that the rabbits
returned to you determined the end pattern of the tree, and herein lies the
problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and
you need to make sure that all of the modifications or pathogens introduced by
Professor Boolean are contained properly. Since the tree did not preserve the
order of rescue, it falls to you to figure out how many different sequences of
rabbits could have produced an identical tree to your sample sequence, so you
can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it
would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers
and returns a string representing the number (in base-10) of sequences that
would result in the same tree as the given sequence.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
"""


from math import factorial


class Tree(object):
    """A simple implement of BST"""


    def __init__(self, *seq):
        self.node = None
        self.left = None
        self.right = None
        
        for val in seq:
            self.insert(val)

    def insert(self, val):
        if not self.node:
            self.node = val

        elif val > self.node:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Tree(val)

        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Tree(val)


def count(tree):
    """return the amount of the nodes."""


    return 1+count(tree.left)+count(tree.right) if tree else 0


def combination(n, k):
    """return the number of combinations while choosing k elements from
    n elements
    """


    return factorial(n)/(factorial(k)*factorial(n-k)) if n>=k else 0


def permutation(tree):
    """choosing l positions from l+r positions to place the left tree nodes
    will have C(l+r, l) combinations. Recursively count each left subtree 
    and right subtree. The result is C(l+r,l)*P(tree.left)*P(tree.right)
    """
    
    
    if not tree:
        return 1


    left_count = count(tree.left)
    right_count = count(tree.right)

    left_p = permutation(tree.left)
    right_p = permutation(tree.right)

    return combination(left_count+right_count, left_count)*left_p*right_p


def answer(seq):

    return str(permutation(Tree(*seq)))
