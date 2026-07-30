// @leet start
function countTexts(pressedKeys: string): number {
  const MOD = 1000000007n;

  const makeDp = (numLetters: number) => {
    const dp: bigint[] = Array(pressedKeys.length + 1).fill(0n);
    dp[0] = 1n;

    for (let i = 1; i <= pressedKeys.length; i++) {
      for (let j = 1; j <= Math.min(i, numLetters); j++) {
        dp[i] = (dp[i] + dp[i - j]) % MOD;
      }
    }

    return dp;
  };

  const dp3 = makeDp(3);
  const dp4 = makeDp(4);

  // Build up result, keeping track of current key and run length count
  let res = 1n;
  let curr = pressedKeys[0];
  let count = 0;

  for (const key of pressedKeys) {
    if (key === curr) {
      count++;
    } else {
      res =
        (res * (curr === "7" || curr === "9" ? dp4[count] : dp3[count])) % MOD;

      curr = key;
      count = 1;
    }
  }

  res = (res * (curr === "7" || curr === "9" ? dp4[count] : dp3[count])) % MOD;

  return Number(res);
}
// @leet end
