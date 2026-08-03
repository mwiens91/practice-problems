// @leet start
function countValidPrefixes(s: string): number {
  let res = 0;
  let onesCount = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "1") {
      onesCount++;
    }

    if (Math.abs(i + 1 - 2 * onesCount) <= 1) {
      res++;
    }
  }

  return res;
}
// @leet end
