// @leet start
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function (s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) {
    return false;
  }

  const dp = Array(s2.length + 1).fill(false);

  for (let i = s1.length; i >= 0; i--) {
    for (let j = s2.length; j >= 0; j--) {
      dp[j] =
        (i === s1.length && j === s2.length) ||
        (i < s1.length && s1[i] === s3[i + j] && dp[j]) ||
        (j < s2.length && s2[j] === s3[i + j] && dp[j + 1]);
    }
  }

  return dp[0];
};
// @leet end
