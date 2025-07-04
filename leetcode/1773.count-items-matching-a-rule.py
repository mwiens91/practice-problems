# @leet start
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # Get the item index the rule key corresponds to
        match ruleKey:
            case "type":
                rule_key_idx = 0
            case "color":
                rule_key_idx = 1
            case _:
                # "name"
                rule_key_idx = 2

        return sum(1 for item in items if item[rule_key_idx] == ruleValue)


# @leet end
