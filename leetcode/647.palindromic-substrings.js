// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  const dp = Array.from({ length: s.length }, () =>
    Array(s.length).fill(false),
  );
  let count = s.length;

  // i is palindrome length - 1
  for (let i = 1; i < s.length; i++) {
    for (let start = 0; start < s.length - i; start++) {
      dp[start][start + i] =
        s[start] === s[start + i] && (i <= 2 || dp[start + 1][start + i - 1]);

      if (dp[start][start + i]) {
        count++;
      }
    }
  }

  return count;
};
// @leet end
