// @leet start
function firstMatchingIndex(s: string): number {
  for (let i = 0; i < Math.ceil(s.length / 2); i++) {
    if (s[i] === s[s.length - 1 - i]) {
      return i;
    }
  }

  return -1;
}
// @leet end
