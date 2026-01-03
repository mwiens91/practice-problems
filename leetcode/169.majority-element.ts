// @leet start
function majorityElement(nums: number[]): number {
  let curr = 0;
  let score = 0;

  for (const num of nums) {
    if (!score) {
      curr = num;
    }

    score += num === curr ? 1 : -1;
  }

  return curr;
}
// @leet end
