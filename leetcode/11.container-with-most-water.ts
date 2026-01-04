// @leet start
function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let max = 0;

  while (left < right) {
    max = Math.max(max, Math.min(height[left], height[right]) * (right - left));

    if (height[left] >= height[right]) {
      right--;
    } else {
      left++;
    }
  }

  return max;
}
// @leet end
