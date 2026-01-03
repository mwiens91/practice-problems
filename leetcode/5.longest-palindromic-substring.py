# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # This isn't the most efficient solution (there's an O(n)
        # solution—Wikipedia has it), but it's simple enough and it
        # works. Idea: for every character, we take it as the centre and
        # try to expand as far as possible in either direction. This
        # only handles odd-length palindromes, but even-lengths can be
        # found with a simple modification.
        #
        # There's a good optimization to short-circuit early using this
        # approach that I haven't implemented. Start from the middle of
        # s when doing these checks and keep going as close to the
        # centre as possible when doing subsequent checks: this will
        # allow us to return early because in some cases we will find
        # the longest theoretically possible substring. Again though:
        # haven't implemented that here.
        #
        # There's other optimizations that can be done as well, like for
        # example, if you've already found an L-length palindrome, then
        # you don't check for more palindromes using characters as the
        # centre near the end of s whre palindromes can't even achieve
        # a length of L. Not done here though.
        longest_palindrome_left_idx = 0
        longest_palindrome_right_idx = 0
        longest_length = 1

        # Get the length of s
        s_len = len(s)

        # Find the longest palindrome substring by taking each character
        # as a centre
        for idx in range(s_len):
            # Look for odd-length palindrome
            this_length = 1

            left = idx - 1
            right = idx + 1

            while left >= 0 and right < s_len and s[left] == s[right]:
                # Current length is now bigger by two
                this_length += 2

                # Try these indices next
                left -= 1
                right += 1

            if this_length > longest_length:
                # Need to roll back both of the indices by one because
                # they failed the check in the above while loop. Note
                # that the current length is still good though—it
                # doesn't need to be modified.
                longest_palindrome_left_idx = left + 1
                longest_palindrome_right_idx = right - 1

                longest_length = this_length

            # Now do the same for even-length palindromes
            this_length = 0

            left = idx
            right = idx + 1

            while left >= 0 and right < s_len and s[left] == s[right]:
                this_length += 2

                left -= 1
                right += 1

            if this_length > longest_length:
                longest_palindrome_left_idx = left + 1
                longest_palindrome_right_idx = right - 1

        return s[longest_palindrome_left_idx : longest_palindrome_right_idx + 1]


# @leet end
