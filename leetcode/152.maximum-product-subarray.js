// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let curr = 1;
  let startNeg = null;
  let bestNeg = null;
  let bestPos = null;
  let result = nums[0];

  const updateResult = (atZero) => {
    if (atZero) {
      result = Math.max(result, 0);
    }

    if (bestNeg !== null) {
      result = Math.max(result, bestNeg / startNeg);
    }

    if (bestPos !== null) {
      result = Math.max(result, bestPos);
    }
  };

  for (const num of nums) {
    if (num === 0) {
      updateResult(true);
      curr = 1;
      startNeg = null;
      bestNeg = null;
      bestPos = null;
    } else {
      curr *= num;

      if (curr < 0) {
        if (startNeg === null) {
          startNeg = curr;
        } else {
          bestNeg = Math.min(bestNeg, curr);
        }
      } else {
        // curr > 0
        bestPos = Math.max(bestPos, curr);
      }
    }
  }

  updateResult(false);

  return result;
};
// @leet end
