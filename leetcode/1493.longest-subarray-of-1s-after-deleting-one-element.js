// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  let prev = 0;
  let curr = 0;
  let best = 0;
  let foundZero = false;

  for (const bit of nums) {
    if (!bit) {
      best = Math.max(best, prev + curr);

      [prev, curr] = [curr, 0];
      foundZero = true;
    } else {
      curr++;
    }
  }

  best = Math.max(best, prev + curr);

  return best - (foundZero ? 0 : 1);
};
// @leet end
