// @leet start
function countSpecialIntegers(nums: number[]): number {
  const MAX_NUM = 100;
  const seenOne = Array(MAX_NUM + 1).fill(false);
  const seenMany = Array(MAX_NUM + 1).fill(false);

  let seenOneCount = 0;
  let seenManyCount = 0;
  let prev = null;

  for (const num of nums) {
    if (num !== prev) {
      if (!seenOne[num]) {
        seenOne[num] = true;
        seenOneCount++;
      } else if (!seenMany[num]) {
        seenMany[num] = true;
        seenManyCount++;
      }

      prev = num;
    }
  }

  return seenOneCount - seenManyCount;
}
// @leet end
