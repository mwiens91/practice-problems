// @leet start
function subsets(nums: number[]): number[][] {
  const result: number[][] = [];
  let curr: number[] = [];

  const backtrack = (i: number) => {
    if (i === nums.length) {
      result.push([...curr]);

      return;
    }

    backtrack(i + 1);
    curr.push(nums[i]);
    backtrack(i + 1);
    curr.pop();
  };

  backtrack(0);

  return result;
}
// @leet end
