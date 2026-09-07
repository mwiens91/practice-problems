// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);
  const seen = new Set();

  const processComponent = (num) => {
    seen.add(num);
    let size = 1;

    for (let i = num - 1; numsSet.has(i); i--) {
      seen.add(i);
      size++;
    }

    for (let i = num + 1; numsSet.has(i); i++) {
      seen.add(i);
      size++;
    }

    return size;
  };

  let best = 0;

  for (const num of numsSet) {
    if (!seen.has(num)) {
      best = Math.max(best, processComponent(num));
    }
  }

  return best;
};
// @leet end
