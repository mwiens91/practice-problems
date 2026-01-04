// @leet start
function longestPalindrome(s: string): string {
  const dp: boolean[][] = Array.from(s, () => Array.from(s, () => true));

  let maxLength = 1;
  let longest = s[0];

  for (let n = 2; n <= s.length; n++) {
    for (let i = 0; i <= s.length - n; i++) {
      const j = i + n - 1;
      dp[i][j] = s[i] === s[j] && dp[i + 1][j - 1];

      if (dp[i][j] && j - i + 1 > maxLength) {
        maxLength = j - i + 1;
        longest = s.slice(i, j + 1);
      }
    }
  }

  return longest;
}
// @leet end
