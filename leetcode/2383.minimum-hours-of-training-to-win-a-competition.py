# @leet start
class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: list[int],
        experience: list[int],
    ) -> int:
        # Find the energy required, not factoring in the initial energy
        energy_defecit = sum(energy) + 1

        # Find the experience required, not factoring in the initial
        # experience
        experience_defecit = 0
        experience_gained_from_combat = 0

        for xp in experience:
            experience_defecit = max(
                experience_defecit, xp + 1 - experience_gained_from_combat
            )
            experience_gained_from_combat += xp

        # Factor in the initial energy and experience and return the sum
        # of energy and experience still required
        return max(0, energy_defecit - initialEnergy) + max(
            0, experience_defecit - initialExperience
        )


# @leet end
