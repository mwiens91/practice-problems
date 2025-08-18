# @leet start
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        DEVICE = "1"

        beam_count = 0

        # We'll call a "valid" row to mean one that has at least one
        # security device
        prev_valid_row_devices = 0

        for row in bank:
            if devices := row.count(DEVICE):
                beam_count += prev_valid_row_devices * devices
                prev_valid_row_devices = devices

        return beam_count


# @leet end
