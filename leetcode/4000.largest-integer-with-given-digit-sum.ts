// @leet start
function largestInteger(n: number, s: number): number {
  if (s > 9 * n) {
    return -1;
  }

  let res = 0;

  while (n) {
    const rem = s > 9 ? 9 : s;

    res *= 10;
    res += rem;

    s -= rem;
    n--;
  }

  return res;
}
// @leet end
