// @leet start
function minAbsoluteDifference(nums: number[]): number {
  const lastSeen: (number | null)[] = [null, null, null];
  let res = Infinity;

  for (let i = 0; i < nums.length; i++) {
    lastSeen[nums[i]] = i;

    if (lastSeen[1] !== null && lastSeen[2] !== null) {
      res = Math.min(res, Math.abs(lastSeen[1] - lastSeen[2]));
    }
  }

  return res < Infinity ? res : -1;
}
// @leet end
