// @leet start
function wordBreak(s: string, wordDict: string[]): boolean {
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let end = 1; end <= s.length; end++) {
    for (const word of wordDict) {
      if (word.length <= end && s.slice(end - word.length, end) === word) {
        dp[end] ||= dp[end - word.length];
      }
    }
  }

  return dp[s.length];
}
// @leet end
