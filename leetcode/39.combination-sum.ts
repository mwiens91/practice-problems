// @leet start
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  const curr: number[] = [];

  const backtrack = (i: number, amount: number) => {
    if (amount >= target) {
      if (amount === target) {
        result.push([...curr]);
      }

      return;
    }

    for (let j = i; j < candidates.length; j++) {
      curr.push(candidates[j]);
      backtrack(j, amount + candidates[j]);
      curr.pop();
    }
  };

  backtrack(0, 0);

  return result;
}
// @leet end
