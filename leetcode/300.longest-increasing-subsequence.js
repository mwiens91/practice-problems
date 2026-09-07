// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  const subseq = [];

  for (const num of nums) {
    let left = 0;
    let right = subseq.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (num <= subseq[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    if (left === subseq.length) {
      subseq.push(num);
    } else if (num !== subseq[left]) {
      subseq[left] = num;
    }
  }

  return subseq.length;
};
// @leet end
