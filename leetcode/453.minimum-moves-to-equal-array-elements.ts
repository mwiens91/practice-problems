// @leet start
function minMoves(nums: number[]): number {
  const min = Math.min(...nums);

  return nums.reduce((acc, curr) => acc + curr - min, 0);
}
// @leet end
