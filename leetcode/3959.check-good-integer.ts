// @leet start
function checkGoodInteger(n: number): boolean {
  let sum = 0;
  let sqSum = 0;

  while (n) {
    const dig = n % 10;

    sum += dig;
    sqSum += dig ** 2;

    n = (n - dig) / 10;
  }

  return sqSum - sum >= 50;
}
// @leet end
