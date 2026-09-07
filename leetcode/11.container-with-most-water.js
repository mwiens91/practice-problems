// @leet start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let best = 0;

  while (left < right) {
    best = Math.max(
      best,
      (right - left) * Math.min(height[left], height[right]),
    );

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return best;
};
// @leet end
