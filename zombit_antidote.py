"""
Zombit antidote
===============

Forget flu season. Zombie rabbits have broken loose and are terrorizing Silicon
Valley residents! Luckily, you've managed to steal a zombie 
antidote and set up a makeshift rabbit rescue station. Anyone who catches a
zombie rabbit can schedule a meeting at your station to have it injected 
with the antidote, turning it back from a zombit to a fluffy bunny.
Unfortunately, you have a limited amount of time each day, so you need to 
maximize these meetings. Every morning, you get a list of requested injection
meetings, and you have to decide which to attend fully. If you go to an 
injection meeting, you will join it exactly at the start of the meeting, and
only leave exactly at the end.

Can you optimize your meeting schedule? The world needs your help!

Write a method called answer(meetings) which, given a list of meeting requests,
returns the maximum number of non-overlapping meetings that can be 
scheduled. If the start time of one meeting is the same as the end time of
another, they are not considered overlapping.

meetings will be a list of lists. Each element of the meetings list will be a
two element list denoting a meeting request. The first element of that 
list will be the start time and the second element will be the end time of that
meeting request.

All the start and end times will be non-negative integers, no larger than
1000000. 
The start time of a meeting will always be less than the end time.

The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.
"""


def ras(start, finish, k, n):
    """RECURSIVE-ACTIVITY-SELECTOR
    This is a example in the Introduction to Algorithms 16th chapter.

    """
    m = k+1
    while m <= n and start[m] < finish[k]:
        m += 1
    if m <= n:
        return [[start[m], finish[m]]] + ras(start, finish, m, n)
    else:
        return []


def anwser(meetings):

    n = len(meetings)

    #init a virtual activity start at 0, and end at 0
    meetings.append([0,0])
   
    #sort meetings by the progressive finish time
    sort_meetings = sorted(meetings, key=lambda x: x[1])

    start = [i[0] for i in meetings]
    finish = [i[1] for i in meetings]

    return len(ras(start, finish, 0, n)

