// @leet start
function twoSum(nums: number[], target: number): number[] {
  const seenAtIdx: Map<number, number> = new Map();

  for (const [idx, num] of nums.entries()) {
    const complementIdx = seenAtIdx.get(target - num);

    if (complementIdx !== undefined) {
      return [idx, complementIdx];
    }

    seenAtIdx.set(num, idx);
  }

  throw new Error();
}
// @leet end
