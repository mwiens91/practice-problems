// @leet start
function minLengthAfterRemovals(s: string): number {
  let res = 0;

  for (const ch of s) {
    res += ch === "a" ? 1 : -1;
  }

  return Math.abs(res);
}
// @leet end
