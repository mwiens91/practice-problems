// @leet start
function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const result: number[][] = [];

  for (let pivot = 0; pivot < nums.length - 2 && nums[pivot] <= 0; ) {
    let left = pivot + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[pivot] + nums[left] + nums[right];

      if (!sum) {
        result.push([nums[pivot], nums[left], nums[right]]);

        do {
          left++;
        } while (left < right && nums[left] === nums[left - 1]);

        do {
          right--;
        } while (left < right && nums[right] === nums[right + 1]);
      } else if (sum > 0) {
        right--;
      } else {
        left++;
      }
    }

    do {
      pivot++;
    } while (pivot < nums.length - 2 && nums[pivot] === nums[pivot - 1]);
  }

  return result;
}
// @leet end
