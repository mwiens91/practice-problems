// @leet start
function largestEven(s: string): string {
  for (let i = s.length - 1; i >= 0; i--) {
    if (Number(s[i]) % 2 === 0) {
      return s.slice(0, i + 1);
    }
  }

  return "";
}
// @leet end
