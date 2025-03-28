# @leet start
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Constants
        RADIANT_SENATOR = "R"
        # DIRE_SENATOR = "D"

        RADIANT_WIN_MESSAGE = "Radiant"
        DIRE_WIN_MESSAGE = "Dire"

        # Put Radiant and Dire senators turn order in a queue
        radiant_queue: deque[int] = deque()
        dire_queue: deque[int] = deque()

        for i, senator in enumerate(senate):
            (radiant_queue if senator == RADIANT_SENATOR else dire_queue).append(i)

        # Perform the senate, where each senator bans the rights of the
        # next opposition senator to act
        n = len(senate)

        while radiant_queue and dire_queue:
            # Get the next radiant and dire senators
            next_radiant_turn = radiant_queue.popleft()
            next_dire_turn = dire_queue.popleft()

            # For whichever party's turn goes first, give them another
            # turn. The opposition party's turn is already removed and
            # stays removed
            if next_radiant_turn < next_dire_turn:
                radiant_queue.append(next_radiant_turn + n)
            else:
                dire_queue.append(next_dire_turn + n)

        return RADIANT_WIN_MESSAGE if radiant_queue else DIRE_WIN_MESSAGE


# @leet end
