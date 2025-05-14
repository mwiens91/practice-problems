# @leet start
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        PARENT = "../"
        REMAIN = "./"

        # Count how many directories we are from the starting directory
        level = 0

        for log in logs:
            if log == PARENT:
                level = max(0, level - 1)
            elif log == REMAIN:
                pass
            else:
                # Move to child directory
                level += 1

        return level


# @leet end
