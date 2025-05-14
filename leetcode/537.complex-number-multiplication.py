# @leet start
import re


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def get_real_and_complex(complex_str: str) -> tuple[int, int]:
            return tuple(map(int, re.findall(r"-?\d+", complex_str)))

        real_1, imag_1 = get_real_and_complex(num1)
        real_2, imag_2 = get_real_and_complex(num2)

        return f"{real_1*real_2 -imag_1*imag_2}+{real_1*imag_2 + real_2*imag_1}i"


# @leet end
