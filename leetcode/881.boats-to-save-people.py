# @leet start
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Everyone needs to be on a boat, and there are two people
        # maximum per boat. We sort the people in descending order of
        # weight and use two pointers: one to the heaviest person
        # available and one to the lightest person available. For each
        # heaviest available person, if there is capacity for the
        # lightest available person, the lightest available person gets
        # on the boat too; otherwise only the heaviest person available
        # gets on the boat.
        #
        # I'll explain the reason we can select the lightest available
        # person as the second person on the boat instead of the
        # heaviest available person that can fit on the boat. Suppose we
        # selected the lightest available person L_1 on a boat to be
        # matched with the heaviest available person H_1 on a boat
        # instead of the heaviest available person M_1 that could fit
        # with H_1; so
        #
        # H_1 >= M_1 >= L_1.
        #
        # Suppose that for a later heaviest availabe person H_i, they
        # would have been able to take L_1 but not M_1. This implies
        #
        # H_i + M_1 > limit.
        #
        # But this can't be true because
        #
        # H_i <= H_1 <= limit - M_1 => H_i + M_1 <= limit.
        #
        # Therefore we can choose to match the heaviest available person
        # with the lightest available person.

        # First, sort the people in descending order of weight
        people.sort(reverse=True)

        # Use two pointers and find the number of boats
        num_boats = 0

        heaviest_ptr = 0
        lightest_ptr = len(people) - 1

        while heaviest_ptr <= lightest_ptr:
            # Add the heaviest available person
            effective_limit = limit - people[heaviest_ptr]

            heaviest_ptr += 1

            # Add the lightest available person if possible. If the
            # pointers point to the same person, "adding the same person
            # twice" doesn't change the number boats required.
            if people[lightest_ptr] <= effective_limit:
                lightest_ptr -= 1

            # Add a boat
            num_boats += 1

        return num_boats


# @leet end
