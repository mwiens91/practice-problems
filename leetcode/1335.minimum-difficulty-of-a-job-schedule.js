// @leet start
/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function (jobDifficulty, d) {
  const n = jobDifficulty.length;

  if (d > n) {
    return -1;
  }

  let prev = [...jobDifficulty];

  for (let i = n - 2; i >= 0; i--) {
    prev[i] = Math.max(prev[i], prev[i + 1]);
  }

  // k is number of cuts to make
  for (let k = 1; k < d; k++) {
    const curr = Array(jobDifficulty.length).fill(Infinity);

    for (let i = 0; i < n - k; i++) {
      let prefixMax = jobDifficulty[i];

      for (let j = i + 1; j <= n - k; j++) {
        curr[i] = Math.min(curr[i], prefixMax + prev[j]);
        prefixMax = Math.max(prefixMax, jobDifficulty[j]);
      }
    }

    prev = curr;
  }

  return prev[0];
};
// @leet end
