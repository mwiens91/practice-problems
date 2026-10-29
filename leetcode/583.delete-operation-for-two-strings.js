// @leet start
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  if (word1.length > word2.length) {
    [word1, word2] = [word2, word1];
  }

  const dp = Array.from({ length: word1.length + 1 }, (_, i) => word1.length - i);

  for (let i = word2.length - 1; i >= 0; i--) {
    let diag = dp[word1.length];
    dp[word1.length]++;

    for (let j = word1.length - 1; j >= 0; j--) {
      [dp[j], diag] = [
        Math.min(
          word2[i] === word1[j] ? diag : Infinity,
          1 + dp[j],
          1 + dp[j + 1],
        ),
        dp[j],
      ];
    }
  }

  return dp[0];
};
// @leet end
