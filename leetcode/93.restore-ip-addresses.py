# @leet start
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        valid_addrs: list[str] = []

        def address_part_is_valid(str_: str, size: int) -> bool:
            return (
                size
                and (size == 1 or not str_.startswith("0"))
                and 0 <= int(str_) <= 255
            )

        def recurse(
            remaining_address_string: str,
            current_address_parts: list[str],
            dots_left: int = 3,
        ) -> None:
            # Get the number of characters left we haven't processed yet
            remaining_address_len = len(remaining_address_string)

            # Base case
            if not dots_left:
                if address_part_is_valid(
                    remaining_address_string, remaining_address_len
                ):
                    valid_addrs.append(
                        ".".join(current_address_parts + [remaining_address_string])
                    )

                return

            # Try putting a dot in each valid position
            for size in (1, 2, 3):
                if remaining_address_len >= size and address_part_is_valid(
                    remaining_address_string[:size], size
                ):
                    recurse(
                        remaining_address_string[size:],
                        current_address_parts + [remaining_address_string[:size]],
                        dots_left - 1,
                    )

        recurse(s, [])

        return valid_addrs


# @leet end
