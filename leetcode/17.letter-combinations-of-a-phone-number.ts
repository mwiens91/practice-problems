// @leet start
function letterCombinations(digits: string): string[] {
  const digitToChars = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
  };

  const result: string[] = [];
  const curr: string[] = [];

  const backtrack = (i: number) => {
    if (i === digits.length) {
      result.push(curr.join(""));
      return;
    }

    for (const char of digitToChars[digits[i]]) {
      curr.push(char);
      backtrack(i + 1);
      curr.pop();
    }
  };

  backtrack(0);

  return result;
}
// @leet end
