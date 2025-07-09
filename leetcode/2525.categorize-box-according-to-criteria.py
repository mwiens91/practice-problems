# @leet start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = (
            any(dim >= 1e4 for dim in (length, width, height))
            or length * width * height >= 1e9
        )
        is_heavy = mass >= 1e2

        if is_bulky and is_heavy:
            return "Both"

        if is_bulky:
            return "Bulky"

        if is_heavy:
            return "Heavy"

        return "Neither"


# @leet end
