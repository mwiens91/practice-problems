# @leet start
class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        # For each player, count how many of each colour that player
        # picks up
        counter_list: list[dict[int, int]] = [{} for i in range(n)]

        for player_idx, color in pick:
            try:
                counter_list[player_idx][color] += 1
            except KeyError:
                counter_list[player_idx][color] = 1

        # Now count how many players win
        num_winners = 0

        for player_idx in range(n):
            for count in counter_list[player_idx].values():
                if count > player_idx:
                    num_winners += 1

                    break

        return num_winners


# @leet end
