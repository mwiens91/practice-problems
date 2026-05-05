# @leet start
class DetectSquares:

    def __init__(self):
        self.point_freqs: dict[tuple[int, int], int] = {}
        self.y_to_xs: dict[int, list[int]] = {}

    def add(self, point: list[int]) -> None:
        x, y = point

        if (x, y) in self.point_freqs:
            self.point_freqs[(x, y)] += 1
        else:
            self.point_freqs[(x, y)] = 1

            # Mark that we've seen x for this y
            if y not in self.y_to_xs:
                self.y_to_xs[y] = []

            self.y_to_xs[y].append(x)

    def count(self, point: list[int]) -> int:
        xp, yp = point
        count = 0

        for x in self.y_to_xs.get(yp, []):
            if x == xp:
                continue

            delta_x = x - xp

            for sign in (-1, 1):
                if (x, yp + sign * delta_x) in self.point_freqs and (
                    xp,
                    yp + sign * delta_x,
                ) in self.point_freqs:
                    count += (
                        self.point_freqs[(x, yp)]
                        * self.point_freqs[(x, yp + sign * delta_x)]
                        * self.point_freqs[(xp, yp + sign * delta_x)]
                    )

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @leet end
