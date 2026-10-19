# @leet start
class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        # Sort spells and potion
        spellWithIdx = sorted((val, i) for i, val in enumerate(spells))
        potions.sort()

        result = [0] * len(spells)
        potionPtr = len(potions)

        for spellVal, resIdx in spellWithIdx:
            while potionPtr > 0 and spellVal * potions[potionPtr - 1] >= success:
                potionPtr -= 1

            result[resIdx] = len(potions) - potionPtr

        return result


# @leet end
