# @leet start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to chars
        digit_to_chars = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        # Total number of digits
        n = len(digits)

        # Store the results here
        res = []

        # We'll use this to generate all combinations
        def recurse(str_to_add_to: str, digit_idx: int) -> None:
            nonlocal res

            # Get digit
            digit = int(digits[digit_idx])  # 2 - 9

            # Append each of the chars corresponding to this digit to the string passed in
            strs = []

            for ch in digit_to_chars[digit]:
                strs.append(str_to_add_to + ch)

            # Base case: if this is the last digit, add to results
            if digit_idx == n - 1:
                res += strs
            else:
                # Keep recursing
                for str_ in strs:
                    recurse(str_, digit_idx + 1)

        # Handle edge case digits = ""
        if not digits:
            return []

        # Recurse and generate all combinations
        recurse("", 0)

        return res
# @leet end

