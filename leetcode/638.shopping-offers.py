# @leet start
class Solution:
    def shoppingOffers(
        self, price: list[int], special: list[list[int]], needs: list[int]
    ) -> int:
        n = len(price)

        # Filter out specials that are never worth taking
        def special_okay(offer: list[int]) -> bool:
            return offer[n] < sum(amount * cost for amount, cost in zip(offer, price))

        special = list(filter(special_okay, special))
        num_specials = len(special)

        memo: dict[tuple[int, ...], int] = {}

        # Define a memoized recursive function to find the lowest price
        # to get the given needs using special[sp_idx:] and the regular
        # prices
        def get_cheapest(sp_idx: int, needs: tuple[int, ...]) -> int:
            if (sp_idx, *needs) in memo:
                return memo[(sp_idx, *needs)]

            if sp_idx >= num_specials:
                # Used all specials, buy remaining at regular price
                cost = sum(need * price[i] for i, need in enumerate(needs))
                memo[(sp_idx, *needs)] = cost

                return cost

            # Use a special. See if this special helps fulfill our
            # needs without overbuying
            new_needs = tuple(need - num for num, need in zip(special[sp_idx], needs))

            if all(need >= 0 for need in new_needs):
                cheapest = min(
                    get_cheapest(sp_idx + 1, needs),
                    special[sp_idx][n] + get_cheapest(sp_idx, tuple(new_needs)),
                )
            else:
                cheapest = get_cheapest(sp_idx + 1, needs)

            memo[(sp_idx, *needs)] = cheapest

            return cheapest

        return get_cheapest(0, tuple(needs))


# @leet end
