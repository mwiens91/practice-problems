// @leet start
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  citations.sort((a, b) => a - b);

  let left = 0;
  let right = citations.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (citations[mid] >= citations.length - mid) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return citations.length - left;
};
// @leet end
