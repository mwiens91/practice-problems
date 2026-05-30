// @leet start
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function (arr, k) {
  if (arr[0] > k) {
    return k;
  }

  let left = 0;
  let right = arr.length - 1;

  // Find last index with less than k missing numbers
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const numMissing = arr[mid] - mid - 1;

    if (numMissing < k) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  const numMissing = arr[right] - right - 1;

  return arr[right] + k - numMissing;
};
// @leet end
