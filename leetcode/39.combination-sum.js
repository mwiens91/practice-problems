// @leet start
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  candidates.sort((a, b) => a - b);

  const curr = [];
  const res = [];

  const backtrack = (i) => {
    if (target === 0) {
      res.push([...curr]);

      return;
    }

    if (i === candidates.length || candidates[i] > target) {
      return;
    }

    // Try taking
    curr.push(candidates[i]);
    target -= candidates[i];
    backtrack(i);

    // Try not taking
    curr.pop();
    target += candidates[i];
    backtrack(i + 1);
  };

  backtrack(0);

  return res;
};
// @leet end
