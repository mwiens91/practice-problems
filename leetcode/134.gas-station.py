# @leet start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Get the number of stations
        n = len(gas)

        # There's no solution if the costs are higher than the gas
        # available; otherwise there is a solution
        if sum(cost) > sum(gas):
            return -1

        # Find the unique solution
        start = 0
        gain = 0

        for i in range(n):
            # Keep a running total of how much we've gained by
            # travelling to the next station
            gain += gas[i] - cost[i]

            # If the gain is ever negative we reset from the *next*
            # position. Okay, this is hard to explain: don't we need to
            # try the next starting position after our previous one?
            # For example, we could have a case with gas - cost being
            #
            # -1 4 -2 -2 ...
            #
            # If starting at the -1 failed, the 4 might work right? Why
            # are we skipping over that? I don't know how to explain
            # this honestly, but you can't get the 4 to work without
            # also getting something down the line also working (try
            # this); for example
            #
            # -1 4 -2 -2 1
            #
            # has two solutions: the indices corresponding to 4 and 1.
            # But we are guaranteed *unique* solutions, so this is
            # invalid input. Therefore, given that exactly one thing has
            # to work, and that 4 working implies something later must
            # work too, it is not possible for the 4 to work.
            #
            # I'd need to study this problem more (ain't happening) to
            # nail down a proof here. I don't even know if I have the
            # toolset tbh.
            if gain < 0:
                start = i + 1
                gain = 0

        return start


# @leet end
