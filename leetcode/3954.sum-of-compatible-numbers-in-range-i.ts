// @leet start
function sumOfGoodIntegers(n: number, k: number): number {
  let res = 0;

  for (let i = Math.max(0, n - k); i <= n + k; i++) {
    if ((i & n) === 0) {
      res += i;
    }
  }

  return res;
}
// @leet end
