// @leet start
function rearrangeArray(nums: number[]): number[] {
  const maxNum = Math.max(...nums);
  const counts = Array(maxNum + 1).fill(0);

  for (const num of nums) {
    counts[num]++;
  }

  const ans: number[] = [];

  while (ans.length < nums.length) {
    for (let i = 1; i <= maxNum; i++) {
      if (counts[i]) {
        counts[i]--;
        ans.push(i);
      }
    }
  }

  return ans;
}
// @leet end
