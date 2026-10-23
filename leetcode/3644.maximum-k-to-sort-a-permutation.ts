// @leet start
function sortPermutation(nums: number[]): number {
  return (
    nums.reduce<number | null>(
      (acc, curr, i) => (curr === i ? acc : (acc ?? curr) & curr),
      null,
    ) ?? 0
  );
}
// @leet end
