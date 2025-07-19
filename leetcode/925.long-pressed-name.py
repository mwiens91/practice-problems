# @leet start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n_name = len(name)
        n_typed = len(typed)

        name_idx = 0
        typed_idx = 0

        while name_idx < n_name and typed_idx < n_typed:
            if name[name_idx] != typed[typed_idx]:
                return False

            name_idx += 1
            typed_idx += 1

            # Consume long pressed chars
            if name_idx == n_name or name[name_idx] != name[name_idx - 1]:
                while typed_idx < n_typed and typed[typed_idx] == name[name_idx - 1]:
                    typed_idx += 1

        return name_idx == n_name and typed_idx == n_typed


# @leet end
