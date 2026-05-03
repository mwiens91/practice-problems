# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict.sort(key=len)

        # Is it possible to end at this exclusive index?
        dp: list[bool] = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) > i:
                    break

                if word == s[i - len(word) : i]:
                    dp[i] |= dp[i - len(word)]

        return dp[len(s)]


# @leet end
