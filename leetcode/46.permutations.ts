// @leet start
function permute(nums: number[]): number[][] {
  const result: number[][] = [];

  const backtrack = (start: number) => {
    if (start === nums.length - 1) {
      result.push([...nums]);
    }

    for (let i = start; i < nums.length; i++) {
      [nums[start], nums[i]] = [nums[i], nums[start]];
      backtrack(start + 1);
      [nums[start], nums[i]] = [nums[i], nums[start]];
    }
  };

  backtrack(0);

  return result;
}
// @leet end
