// @leet start
function digitFrequencyScore(n: number): number {
  let res = 0;

  while (n) {
    res += n % 10;
    n = Math.floor(n / 10);
  }

  return res;
}
// @leet end
