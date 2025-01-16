# @leet start
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Sort both lists in reverse order
        g.sort(reverse=True)
        s.sort(reverse=True)

        # Count the number of cookies we can assign (while keeping
        # children content)
        num_children = len(g)
        num_cookies = len(s)

        child_pointer = 0
        cookie_pointer = 0

        cookies_assigned = 0

        while child_pointer < num_children and cookie_pointer < num_cookies:
            # Assign a cookie to the child if possible
            if g[child_pointer] <= s[cookie_pointer]:
                cookies_assigned += 1

                cookie_pointer += 1

            # Move to the next child
            child_pointer += 1

        return cookies_assigned


# @leet end
