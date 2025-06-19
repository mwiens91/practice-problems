# @leet start
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        person_k_desired_tickets = tickets[k]
        time_taken = 0

        # Each person gets an opportunity to buy
        # person_k_desired_tickets - 1. If they are behind person k (or
        # are person k), they additionally are allowed to buy another
        # ticket.
        for i, desired_tickets in enumerate(tickets):
            if desired_tickets > person_k_desired_tickets - 1:
                time_taken += person_k_desired_tickets - 1 + (1 if i <= k else 0)
            else:
                # desired_tickets <= person_k_desired_tickets - 1
                time_taken += desired_tickets

        return time_taken


# @leet end
