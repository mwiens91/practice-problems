# @leet start
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        res: list[list[int]] = []

        for person in people:
            res.insert(person[1], person)

        return res


# @leet end
