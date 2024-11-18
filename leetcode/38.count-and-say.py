# @leet start
class Solution:
    def countAndSay(self, n: int) -> str:
        # Define a function to get the RLE of a number contained in a
        # string
        def rle(s: str) -> str:
            # Put the result in here
            rle_result = ""

            # Iterate over number characters in string
            current_char = s[0]
            count = 0

            for char in s:
                if char == current_char:
                    # Increase count
                    count += 1
                else:
                    # Mark the previous count + character in the result
                    # string, and set up for the next character
                    rle_result += str(count) + current_char

                    current_char = char
                    count = 1

            # Mark down the final count + character
            rle_result += str(count) + current_char

            return rle_result

        result = "1"

        for _ in range(1, n):
            result = rle(result)

        return result


# @leet end
