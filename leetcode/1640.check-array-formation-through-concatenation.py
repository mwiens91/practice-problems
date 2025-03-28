# @leet start
class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        # Make a dictionary where each key is the first element of a
        # piece and the corresponding value is the piece
        pieces_dict = {piece[0]: piece for piece in pieces}

        # Try to form the array
        n = len(arr)

        i = 0

        while i < n:
            # Try getting a piece whose first element fits
            try:
                piece = pieces_dict[arr[i]]
            except KeyError:
                return False

            # Make sure the piece fits
            for num in piece:
                try:
                    assert num == arr[i]
                except (AssertionError, IndexError):
                    return False

                i += 1

        return True


# @leet end
