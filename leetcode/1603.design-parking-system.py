# @leet start
BIG = 1
MEDIUM = 2
# SMALL = 3


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.remaining_big = big
        self.remaining_medium = medium
        self.remaining_small = small

    def addCar(self, carType: int) -> bool:
        if carType == BIG:
            if not self.remaining_big:
                return False

            self.remaining_big -= 1

            return True

        if carType == MEDIUM:
            if not self.remaining_medium:
                return False

            self.remaining_medium -= 1

            return True

        # carType == SMALL
        if not self.remaining_small:
            return False

        self.remaining_small -= 1

        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @leet end
