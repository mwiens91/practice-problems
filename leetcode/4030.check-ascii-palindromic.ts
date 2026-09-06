// @leet start
function isPalindromic(s: string): boolean {
  const expanded = [...s]
    .map((ch) => ch.codePointAt(0)!.toString(2).padStart(8, "0"))
    .join("");

  for (
    let left = 0, right = expanded.length - 1;
    left < right;
    left++, right--
  ) {
    if (expanded[left] !== expanded[right]) {
      return false;
    }
  }

  return true;
}
// @leet end
