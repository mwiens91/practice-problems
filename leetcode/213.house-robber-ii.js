// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const getAnswer = (left, right) => {
    let prev = 0;
    let prev2 = 0;

    for (let i = right; i >= left; i--) {
      [prev, prev2] = [Math.max(nums[i] + prev2, prev), prev];
    }

    return prev;
  };

  return nums.length > 1
    ? Math.max(getAnswer(1, nums.length - 1), getAnswer(0, nums.length - 2))
    : nums[0];
};
// @leet end
