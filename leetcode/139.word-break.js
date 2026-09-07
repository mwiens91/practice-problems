// @leet start
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const dp = Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (const word of wordDict) {
      if (word.length > i) {
        continue;
      }

      let matches = true;

      for (let j = 0; j < word.length; j++) {
        if (word[j] !== s[i - word.length + j]) {
          matches = false;
        }
      }

      dp[i] ||= matches && dp[i - word.length];
    }
  }

  return dp[s.length];
};
// @leet end
