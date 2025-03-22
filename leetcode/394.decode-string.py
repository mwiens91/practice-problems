# @leet start
import re


class Solution:
    def decodeString(self, s: str) -> str:
        # Grab all alphabetic components, integers, and closing brackets
        # ] in order. We can use a sliding window or regex. Python's
        # regex engine is in C and is very fast, but this approach also
        # requires more memory. Since the constraints on the length of s
        # are small, we use regex here.
        elements = re.findall(r"[a-z]+|\d+|\]", s)

        # Decode the string using a stack. We iterate over elements. If
        # an element is an integer or an alphabetic component we push it
        # on the stack; otherwise if it is a closing bracket ] we pop an
        # alphabetic component A and integer x from the stack, duplicate
        # A x times, and push the result on the stack. Before continuing
        # with the next element, while the top two elements of the stack
        # are alphabetic components, we merge the top alphabetic
        # component into the second from the top alphabetic component.
        #
        # NOTE: It would be faster to convert each alphabetic component
        # to a list of characters so when we merge, we merge two lists,
        # rather than two strings. I haven't implemented that here,
        # however, due to the small constraints on the problem and to
        # keep things clean.
        stack: list[str] = [""]

        for element in elements:
            if element == "]":
                last_alpha_component = stack.pop()
                mult = int(stack.pop())

                stack.append(last_alpha_component * mult)
            else:
                stack.append(element)

            while len(stack) >= 2 and stack[-1].isalpha() and stack[-2].isalpha():
                alpha_component_to_merge = stack.pop()
                stack[-1] += alpha_component_to_merge

        return stack[-1]


# @leet end
