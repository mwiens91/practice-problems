// @leet start
function countSpecialIntegers(nums: number[]): number {
  const numToIdxs = new Map<number, number[]>();

  for (const [i, num] of nums.entries()) {
    if (numToIdxs.has(num)) {
      numToIdxs.get(num)!.push(i);
    } else {
      numToIdxs.set(num, [i]);
    }
  }

  let count = 0;

  for (const idxs of numToIdxs.values()) {
    if (idxs.length < 3) {
      continue;
    }

    let okay = true;

    for (let i = 2; i < idxs.length; i++) {
      if (idxs[i] - idxs[i - 1] !== idxs[i - 1] - idxs[i - 2]) {
        okay = false;
        break;
      }
    }

    count += Number(okay);
  }

  return count;
}
// @leet end
