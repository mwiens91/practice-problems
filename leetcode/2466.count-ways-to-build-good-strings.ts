// @leet start
function countGoodStrings(
  low: number,
  high: number,
  zero: number,
  one: number,
): number {
  const MOD = 1_000_000_007;
  const dp: number[] = Array.from({ length: high + 1 }, () => 0);
  dp[0] = 1;

  let result = 0;
  const step = gcd(zero, one);

  for (let i = Math.min(zero, one); i <= high; i += step) {
    if (i >= zero) {
      dp[i] = (dp[i] + dp[i - zero]) % MOD;
    }

    if (i >= one) {
      dp[i] = (dp[i] + dp[i - one]) % MOD;
    }

    if (i >= low) {
      result = (result + dp[i]) % MOD;
    }
  }

  return result;
}

function gcd(a: number, b: number): number {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }

  return a;
}
// @leet end
