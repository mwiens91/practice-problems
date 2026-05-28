// @leet start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const res = [];

  // NOTE: second condition is optional optimization
  for (let i = 0; i < nums.length && nums[i] <= 0; ) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (!sum) {
        res.push([nums[i], nums[left], nums[right]]);

        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }

      while (right < nums.length - 1 && nums[right] === nums[right + 1]) {
        right--;
      }

      while (left > i + 1 && nums[left] === nums[left - 1]) {
        left++;
      }
    }

    do {
      i++;
    } while (i < nums.length && nums[i] === nums[i - 1]);
  }

  return res;
};
// @leet end
