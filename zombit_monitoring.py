"""
Zombit monitoring
=================

The first successfully created zombit specimen, Dolly the Zombit, needs
constant monitoring, and Professor Boolean has tasked the minions with it. Any
minion who monitors the zombit records the start and end times of their shifts.
However, those minions, they are a bit disorganized: there may be times when
multiple minions are monitoring the zombit, and times when there are none!

That's fine, Professor Boolean thinks, one can always hire more minions...
Besides, Professor Boolean can at least figure out the total amount of time
that Dolly the Zombit was monitored. He has entrusted you, another one of his
trusty minions, to do just that. Are you up to the task?

Write a function answer(intervals) that takes a list of pairs [start, end] and
returns the total amount of time that Dolly the Zombit was monitored by at
least one minion. Each [start, end] pair represents the times when a minion
started and finished monitoring the zombit. All values will be positive
integers no greater than 2^30 - 1. You will always have end > start for each
interval.
"""

def answer(intervals):
    """Unlike the zombit antidote problem, we need to sort the intervals in 
    monotonically increasing order of start time. Result is initialized
    to be the first intervals, then traversalling the left intervals. If the
    next finish time is smaller than the previous finish time, that means the
    previous interval cover the next interval, so the total time keeps invariant. 
                          |_______________|
                              |______|
    Otherwise, there are two situation. One is
    |__________|
                    |______|

    And the other
    |_____________|
           |___________|

    An extra part(finish[i]-max(start[i],finist[i-1])) is added to result.

    """

    sort_intervals = sorted(intervals, key=lambda x:x[0])

    start = [i[0] for i in sort_intervals]
    finish = [i[1] for i in sort_intervals]

    result = finish[0] - start[0]

    for i in range(1, len(intervals)):
        if finish[i] <= finish[i-1]:
            finish[i] = finish[i-1]
        else:
            partition = max(start[i], finish[i-1])
            result = result + finish[i] - partition

    return result
    
