# @leet start
class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        # Store the change in population for each year from 1950 to
        # 2050. Each index i (0 <= i < 101) in the following list
        # corresponds to the year 1950 + i.
        change_in_pop_list = [0] * 101

        for birth_year, death_year in logs:
            change_in_pop_list[birth_year - 1950] += 1
            change_in_pop_list[death_year - 1950] -= 1

        # Find the year with maximum population
        max_pop = 0
        max_pop_year = 1949

        current_pop = 0

        # No need to iterate over the last index of the change in
        # populations list, since no births can occur in 2050—only
        # deaths
        for i in range(100):
            current_pop += change_in_pop_list[i]

            if current_pop > max_pop:
                max_pop = current_pop
                max_pop_year = 1950 + i

        return max_pop_year


# @leet end
