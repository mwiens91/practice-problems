# @leet start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Macro for dot and star chars
        DOT = "."
        STAR = "*"

        # We'll take a recursive approach with memoization
        memo: dict[tuple[str, str], bool] = {}

        def is_match(target: str, pattern: str) -> bool:
            # Try to get a previously computed solution
            if (target, pattern) in memo:
                return memo[(target, pattern)]

            # Base cases:
            # - return True if both target and pattern are empty
            # - return False if target is non-empty but pattern is empty
            #
            # Note that because of the star quantifier it's okay for
            # target to be empty but pattern to be non-empty.
            if not target and not pattern:
                return True

            if not pattern:
                return False

            # Get character to match
            to_match = pattern[0]
            has_star = len(pattern) > 1 and pattern[1] == STAR

            # Match depending on whether we have a star quantifier
            if not has_star:
                if (
                    target
                    and to_match in {DOT, target[0]}
                    and is_match(target[1:], pattern[1:])
                ):
                    # We've found a solution
                    return True
            else:
                # Has star quantifier
                next_pattern = pattern[2:]

                # Try matching zero elements
                if is_match(target, next_pattern):
                    return True

                # Try matching one to as many elements as possible
                for i, target_char in enumerate(target):
                    if to_match in {DOT, target_char}:
                        # Valid match for next element
                        if is_match(target[i + 1 :], next_pattern):
                            # Valid match for entire target and pattern
                            return True
                    else:
                        # Invalid match for next element
                        break

            # Memoize and return solution
            memo[(target, pattern)] = False

            return False

        return is_match(s, p)


# @leet end
