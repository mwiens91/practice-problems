// @leet start
/**
 * @param {string} s
 * @return {boolean}
 */
var isAdjacentDiffAtMostTwo = function (s) {
  for (let i = 1; i < s.length; i++) {
    if (Math.abs(Number(s[i - 1]) - Number(s[i])) > 2) {
      return false;
    }
  }

  return true;
};
// @leet end
