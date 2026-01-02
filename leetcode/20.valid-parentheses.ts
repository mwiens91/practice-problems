// @leet start
function isValid(s: string): boolean {
  type Open = "(" | "[" | "{";
  type Close = ")" | "]" | "}";
  const PAREN_MAP: Record<Open, Close> = {
    "(": ")",
    "[": "]",
    "{": "}",
  };
  const stack: Open[] = [];

  for (const char of s) {
    if (char in PAREN_MAP) {
      stack.push(char as Open);
    } else {
      const left = stack.pop();
      if (left === undefined || char !== PAREN_MAP[left]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
// @leet end
