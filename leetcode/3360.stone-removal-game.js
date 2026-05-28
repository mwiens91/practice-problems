// @leet start
/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function (n) {
  for (let count = 10; ; count -= 2) {
    if (count > n) {
      return false;
    }

    if (2 * count - 1 > n) {
      return true;
    }

    n -= 2 * count - 1;
  }
};
// @leet end
