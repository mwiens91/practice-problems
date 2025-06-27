# @leet start
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        n_odd = n % 2 == 1

        for row in image:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = (row[n - 1 - i] + 1) % 2, (row[i] + 1) % 2

            if n_odd:
                row[n // 2] = (row[n // 2] + 1) % 2

        return image


# @leet end
