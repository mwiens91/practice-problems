// @leet start
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (matrix, k) {
  const n = matrix.length;

  const findMinK = (x) => {
    let numSmaller = 0;
    let j = 0;

    for (let i = n - 1; i >= 0; i--) {
      while (j < n && matrix[i][j] < x) {
        j++;
      }

      numSmaller += j;
    }

    return numSmaller + 1;
  };

  // Set left to min element; right to max
  let left = Infinity;
  let right = -Infinity;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      left = Math.min(left, matrix[i][j]);
      right = Math.max(right, matrix[i][j]);
    }
  }

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (findMinK(mid) <= k) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return right;
};
// @leet end
