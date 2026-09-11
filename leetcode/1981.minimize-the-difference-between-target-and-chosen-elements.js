// @leet start
/**
 * @param {number[][]} mat
 * @param {number} target
 * @return {number}
 */
var minimizeTheDifference = function (mat, target) {
  let prev = new Set([0]);

  for (const row of mat) {
    const curr = new Set();
    let minExceeding = Infinity;

    for (const val of row) {
      for (const prevSum of prev) {
        const currSum = val + prevSum;

        if (currSum >= target) {
          minExceeding = Math.min(minExceeding, currSum);
        } else {
          curr.add(currSum);
        }
      }
    }

    curr.add(minExceeding);
    prev = curr;
  }

  return [...prev].reduce(
    (best, sum) => Math.min(best, Math.abs(target - sum)),
    Infinity,
  );
};
// @leet end
