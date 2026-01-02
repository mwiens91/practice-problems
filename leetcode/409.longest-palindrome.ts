// @leet start
function longestPalindrome(s: string): number {
  const counts: Map<string, number> = new Map();
  let pairs = 0;
  let singles = 0;

  for (const c of s) {
    counts.set(c, 1 + (counts.get(c) ?? 0));

    if (counts.get(c)! % 2 === 0) {
      pairs++;
      singles--;
    } else {
      singles++;
    }
  }

  return 2 * pairs + Math.min(singles, 1);
}
// @leet end
