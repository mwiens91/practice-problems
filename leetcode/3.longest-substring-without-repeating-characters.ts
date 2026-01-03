// @leet start
function lengthOfLongestSubstring(s: string): number {
  const lastIdx = new Map<string, number>();
  let start = 0;
  let longest = 0;

  for (let i = 0; i < s.length; i++) {
    if (lastIdx.has(s[i])) {
      start = Math.max(start, lastIdx.get(s[i])! + 1);
    }

    longest = Math.max(longest, i - start + 1);
    lastIdx.set(s[i], i);
  }

  return longest;
}
// @leet end
