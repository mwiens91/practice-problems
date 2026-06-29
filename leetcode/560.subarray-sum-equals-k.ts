// @leet start
function subarraySum(nums: number[], k: number): number {
  // Keep track of prefix sums before each index
  const prefixFreqs = new Map([[0, 1]]);
  let currSum = 0;
  let res = 0;

  for (const num of nums) {
    currSum += num;
    res += prefixFreqs.get(currSum - k) ?? 0;
    prefixFreqs.set(currSum, (prefixFreqs.get(currSum) ?? 0) + 1);
  }

  return res;
}
// @leet end
