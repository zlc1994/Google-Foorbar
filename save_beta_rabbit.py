"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of
rooms. In the center of each room (except for the top left room) is a hungry
zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move
through this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid,
there is a door to the room above, below, left, and right. There is no door in
cases where there is no room in that direction. However, the doors are locked
in such a way that Beta Rabbit can only ever move to the room below or to the
right. Once Beta Rabbit enters a room, the zombie immediately starts crawling
towards him, and he must feed the zombie until it is full to ward it off.
Thankfully, Beta Rabbit took a class about zombies and knows how many units of
food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which
also has a hungry zombie) and have used most of the limited food he has. He
decides to take the path through the grid such that he ends up with as little
food as possible at the end.

Write a function answer(food, grid) that returns the number of units of food
Beta Rabbit will have at the end, given that he takes a route using up as much
food as possible without him being eaten, and ends at the bottom right room. If
there does not exist a route in which Beta Rabbit will not be eaten, then
return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive
integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list
of N integers each, denoting a single row of N rooms. The first element of grid
will be the list denoting the top row, the second element will be the list
denoting second row from the top, and so on until the last element, which is
the list denoting the bottom row. In the list denoting a single row, the first
element will be the amount of food the zombie in the left-most room in that row
needs, the second element will be the amount the zombie in the room to its
immediate right needs and so on. The top left room will always contain the
integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie
requires will be a positive integer not exceeding 10.
"""
from functools import wraps

def memorized(f):
    """Decorator that caches a function's return value each time it is
    called. If called later with the same arguments, the cached value
    is returned, and not re-evaluated.

    """
    cache = {}
    @wraps(f)
    def wrapped(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrapped


def answer(food, grid):
    @memorized
    def r(t, i, j):
        """
        Backtracing,
        let the rabbit start from the bottom right and move to top left
        """

        #when get to (i,j) position, minus the food with the zombie needs
        t -= grid[i][j]


        #the food is not enough for rabbit to get to the top left or 
        #rabbit can't go left or top. 
        if i < 0 or j < 0 or t < 0:
            return food+1

        #can get to the top left, t is the remainder.
        elif i == 0 and j == 0:
            return t

        #choose the less food grid.
        else:
            return min(r(t, i-1, j), r(t, i, j-1))
    reminder = r(food, len(grid)-1, len(grid)-1)
    return reminder if reminder <= food else -1
