// @leet start
function numSplits(s: string): number {
  const prefixDistinct: number[] = [];
  const seen = new Set<string>();

  for (const ch of s) {
    seen.add(ch);
    prefixDistinct.push(seen.size);
  }

  seen.clear();
  let result = 0;

  for (let i = s.length - 1; i > 0; i--) {
    seen.add(s[i]);

    if (seen.size === prefixDistinct[i - 1]) {
      result++;
    } else if (seen.size > prefixDistinct[i - 1]) {
      break;
    }
  }

  return result;
}
// @leet end
