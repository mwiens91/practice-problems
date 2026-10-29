// @leet start
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function (s, t) {
  const dp = Array(s.length + 1).fill(1);

  for (let i = t.length - 1; i >= 0; i--) {
    let diag = dp[s.length];
    dp[s.length] = 0;

    for (let j = s.length - 1; j >= 0; j--) {
      [dp[j], diag] = [dp[j + 1] + (t[i] === s[j] ? diag : 0), dp[j]];
    }
  }

  return dp[0];
};
// @leet end
