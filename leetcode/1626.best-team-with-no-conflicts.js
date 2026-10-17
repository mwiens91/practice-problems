// @leet start
/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function (scores, ages) {
  const ageScores = ages
    .map((age, i) => [age, scores[i]])
    .sort((a, b) => (a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]));
  const dp = Array(scores.length).fill(0);

  for (let i = dp.length - 1; i >= 0; i--) {
    for (let j = i + 1; j < dp.length; j++) {
      if (
        ageScores[j][0] <= ageScores[i][0] ||
        ageScores[j][1] >= ageScores[i][1]
      ) {
        dp[i] = Math.max(dp[i], dp[j]);
      }
    }

    dp[i] += ageScores[i][1];
  }

  return Math.max(...dp);
};
// @leet end
