// @leet start
function countSpecialIntegers(nums: number[]): number {
  const MAX_NUM = 100;
  const seenAt = Array.from({ length: MAX_NUM + 1 }, () => []);
  nums.forEach((x, i) => seenAt[x].push(i));

  return seenAt.reduce(
    (acc, idxs) =>
      acc +
      Number(idxs.length === 3 && idxs[2] - idxs[1] === idxs[1] - idxs[0]),
    0,
  );
}
// @leet end
