// @leet start
function productExceptSelf(nums: number[]): number[] {
  const result: number[] = new Array(nums.length);

  let prod = 1;

  for (let i = 0; i < nums.length; i++) {
    result[i] = prod;
    prod *= nums[i];
  }

  prod = 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= prod;
    prod *= nums[i];
  }

  return result;
}
// @leet end
