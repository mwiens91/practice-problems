// @leet start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const res = Array(nums.length).fill(1);

  for (let i = nums.length - 2; i >= 0; i--) {
    res[i] = res[i + 1] * nums[i + 1];
  }

  // Multiply by corresponding prefix product
  let prefixProd = 1;

  for (let i = 0; i < nums.length; i++) {
    res[i] *= prefixProd;
    prefixProd *= nums[i];
  }

  return res;
};
// @leet end
