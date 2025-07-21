# @leet start
class Solution:
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        CATEGORIES = {"electronics", "grocery", "pharmacy", "restaurant"}

        # Filter valid coupons: store them as tuples (category, code)
        valid_coupons = [
            (category, code)
            for code, category, active_flag in zip(code, businessLine, isActive)
            if active_flag
            and category in CATEGORIES
            and code
            and all(c.isalnum() or c == "_" for c in code)
        ]

        # Return the codes based on the sort order of the tuples
        return [code for _, code in sorted(valid_coupons)]


# @leet end
