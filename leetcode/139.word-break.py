# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Use memoization
        memo: dict[str, bool] = {"": True}

        def can_break_word(str_: str) -> bool:
            if str_ in memo:
                return memo[str_]

            # Try each word to fit into the string
            for word in wordDict:
                if str_.startswith(word) and can_break_word(str_[len(word) :]):
                    memo[str_] = True

                    return True

            memo[str_] = False

            return False

        return can_break_word(s)


# @leet end
