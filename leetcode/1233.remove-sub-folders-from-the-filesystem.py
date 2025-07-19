# @leet start
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()

        result = [folder[0]]

        for folder_str in folder[1:]:
            # If the current folder is a subfolder of the last parent
            # folder we added, then the parent is a prefix of the
            # subfolder, and the character immediately following the
            # parent folder is a "/"
            if (
                not folder_str.startswith(result[-1])
                or folder_str[len(result[-1])] != "/"
            ):
                result.append(folder_str)

        return result


# @leet end
