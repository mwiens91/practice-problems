# @leet start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # We'll try a recursive brute force approach here
        success = False

        # Get lengths of s1, s2, s3
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        # Handle edge case
        if n3 != n1 + n2:
            return False

        # Keep track of what values we've called the recursive function
        # with so we minimize extra work
        used_vals = set()

        def recurse(i1: int = 0, i2: int = 0, i3: int = 0) -> None:
            nonlocal success

            # If another function reached a successful point, don't
            # continue
            if success:
                return

            # Get out early if we've already called recurse with the
            # argument values
            if (vals := (i1, i2, i3)) in used_vals:
                return

            used_vals.add(vals)

            # If we've finished s3, we're done!
            if i3 == n3:
                success = True

                return

            # Recurse
            ch3 = s3[i3]

            if i1 < n1 and s1[i1] == ch3:
                recurse(i1 + 1, i2, i3 + 1)

            if i2 < n2 and s2[i2] == ch3:
                recurse(i1, i2 + 1, i3 + 1)

        recurse()

        return success


# @leet end
