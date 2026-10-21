// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumSubarrayLength = function (nums, k) {
  MAX_BITS = 30;
  const counts = Array(MAX_BITS).fill(0);

  const addNum = (num) => {
    let i = 0;

    while (num) {
      counts[i] += num % 2;
      num >>= 1;
      i++;
    }
  };

  const removeNum = (num) => {
    let i = 0;

    while (num) {
      counts[i] -= num % 2;
      num >>= 1;
      i++;
    }
  };

  const getOr = () =>
    counts.reduce((acc, curr, i) => acc + ((curr ? 1 : 0) << i), 0);

  let best = Infinity;
  let left = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] >= k) {
      return 1;
    }

    addNum(nums[i]);

    while (getOr() >= k) {
      best = Math.min(best, i - left + 1);
      removeNum(nums[left]);
      left++;
    }
  }

  return best < Infinity ? best : -1;
};
// @leet end
