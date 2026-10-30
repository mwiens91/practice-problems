// @leet start
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var closestToTarget = function (arr, target) {
  const MAX_BITS = 20;
  const notSetCounts = Array(MAX_BITS).fill(0);

  const getAnd = () =>
    notSetCounts.reduce((acc, curr, i) => acc + (Number(!curr) << i), 0);
  const addNum = (num) => {
    for (let i = 0; i < MAX_BITS; i++) {
      notSetCounts[i] += !(num & 1);
      num >>= 1;
    }
  };
  const removeNum = (num) => {
    for (let i = 0; i < MAX_BITS; i++) {
      notSetCounts[i] -= !(num & 1);
      num >>= 1;
    }
  };

  let best = Infinity;
  let start = 0;

  for (let i = 0; i < arr.length; i++) {
    addNum(arr[i]);
    best = Math.min(best, Math.abs(getAnd() - target));

    while (getAnd() <= target) {
      removeNum(arr[start]);
      start++;

      best = Math.min(best, Math.abs(getAnd() - target));
    }
  }

  return best;
};
// @leet end
