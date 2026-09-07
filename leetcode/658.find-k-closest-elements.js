// @leet start
/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function (arr, k, x) {
  // Do binary search to find closest with smallest index
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (arr[mid] <= x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  // Grow the window to size k
  let windowLeft =
    right === arr.length - 1 ||
    (right >= 0 && x - arr[right] <= arr[right + 1] - x)
      ? right
      : right + 1;
  let windowRight = windowLeft;

  while (windowRight - windowLeft + 1 < k) {
    if (
      windowRight === arr.length - 1 ||
      (windowLeft > 0 && x - arr[windowLeft - 1] <= arr[windowRight + 1] - x)
    ) {
      windowLeft--;
    } else {
      windowRight++;
    }
  }

  return arr.slice(windowLeft, windowRight + 1);
};
// @leet end
