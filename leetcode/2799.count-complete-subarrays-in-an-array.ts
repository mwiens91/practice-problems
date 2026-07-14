// @leet start
function countCompleteSubarrays(nums: number[]): number {
  const numDistinct = new Set(nums).size;
  const counts = new Map<number, number>();
  let res = 0;
  let left = 0;

  for (let right = 0; right < nums.length; right++) {
    counts.set(nums[right], 1 + (counts.get(nums[right]) ?? 0));

    while (counts.size === numDistinct) {
      res += nums.length - right;

      const count = counts.get(nums[left])!;

      if (count > 1) {
        counts.set(nums[left], count - 1);
      } else {
        counts.delete(nums[left]);
      }

      left++;
    }
  }

  return res;
}
// @leet end
