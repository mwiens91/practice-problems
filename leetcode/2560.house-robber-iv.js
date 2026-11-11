// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCapability = function (nums, k) {
  const isValid = (limit) => {
    let remaining = k;
    let i = 0;

    while (i < nums.length) {
      if (nums[i] <= limit) {
        remaining--;
        i += 2;

        if (!remaining) {
          return true;
        }
      } else {
        i += 1;
      }
    }

    return false;
  };

  const sortedNums = [...nums].sort((a, b) => a - b);

  let left = k - 1;
  let right = sortedNums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (isValid(sortedNums[mid])) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return sortedNums[left];
};
// @leet end
