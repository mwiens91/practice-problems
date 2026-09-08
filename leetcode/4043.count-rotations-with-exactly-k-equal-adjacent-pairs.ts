// @leet start
function countRotations(s: string, k: number): number {
  let pairs = Number(s[0] === s[s.length - 1]);

  for (let i = 0; i < s.length; i++) {
    pairs += Number(s[i] === s[i - 1]);
  }

  if (k === pairs) {
    return s.length - pairs;
  }

  if (k === pairs - 1) {
    return pairs;
  }

  return 0;
}
// @leet end
