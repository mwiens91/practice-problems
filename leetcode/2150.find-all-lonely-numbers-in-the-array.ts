// @leet start
function findLonely(nums: number[]): number[] {
  const counts = new Map();

  for (const num of nums) {
    counts.set(num, 1 + (counts.get(num) ?? 0));
  }

  const result = [];

  for (const [num, count] of counts.entries()) {
    if (count === 1 && !counts.has(num - 1) && !counts.has(num + 1)) {
      result.push(num);
    }
  }

  return result;
}
// @leet end
