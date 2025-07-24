# @leet start
class Solution:
    def concatHex36(self, n: int) -> str:
        def get_base_x_repr(n: int, x: int) -> str:
            res_reversed: list[str] = []

            while n:
                mod_val = n % x

                if 0 <= mod_val <= 9:
                    res_reversed.append(str(mod_val))
                else:
                    res_reversed.append(chr(ord("A") + mod_val - 10))

                n //= x

            return "".join(reversed(res_reversed))

        return get_base_x_repr(n**2, 16) + get_base_x_repr(n**3, 36)


# @leet end
