# @leet start
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def is_valid(max_weight: int) -> bool:
            count = 1
            curr = 0

            for weight in weights:
                if curr + weight > max_weight:
                    count += 1
                    curr = weight
                else:
                    curr += weight

            return count <= days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if is_valid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


# @leet end
