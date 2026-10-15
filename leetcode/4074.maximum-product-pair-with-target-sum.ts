// @leet start
function maxProductPair(nums: number[], target: number): number[] {
  // Could use the usual val->idx map but the value range is small
  // enough that we can operate faster (probably?)
  const OFFSET = 100;
  const idxOfVal = Array<number>(2 * OFFSET + 1).fill(-1);

  let best = -Infinity;
  let bestBig = -1;
  let bestSmall = -1;

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    const compIdx = idxOfVal[OFFSET + complement] ?? -1;
    const compProduct = nums[i] * complement;

    if (compIdx !== -1 && nums[i] !== complement && compProduct > best) {
      best = compProduct;
      [bestBig, bestSmall] = nums[i] > complement ? [i, compIdx] : [compIdx, i];
    }

    idxOfVal[OFFSET + nums[i]] = i;
  }

  return [bestBig, bestSmall];
}
// @leet end
