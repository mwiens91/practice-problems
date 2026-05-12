# @leet start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        last = int(s[n - 1] != "0")
        second_last = 1

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = last

                if s[i] == "1" or s[i] == "2" and s[i + 1] <= "6":
                    curr += second_last

            second_last = last
            last = curr

        return last


# @leet end
