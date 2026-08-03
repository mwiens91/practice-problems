// @leet start
function maxPairStrength(nums: number[]): number {
  const gcd = (a: number, b: number) => {
    while (b) {
      [a, b] = [b, a % b];
    }

    return a;
  };

  let best = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      best = Math.max(best, (nums[i] * nums[j]) / gcd(nums[i], nums[j]) ** 2);
    }
  }

  return best;
}
// @leet end
