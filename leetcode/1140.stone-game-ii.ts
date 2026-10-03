// @leet start
function stoneGameII(piles: number[]): number {
  const prefixSums: number[] = [0];

  for (const pile of piles) {
    prefixSums.push(prefixSums[prefixSums.length - 1] + pile);
  }

  const dp: number[][] = Array.from({ length: piles.length }, () =>
    Array(piles.length + 1).fill(0),
  );

  for (let i = piles.length - 1; i >= 0; i--) {
    for (let j = piles.length; j > 0; j--) {
      if (i >= piles.length - 2 * j) {
        dp[i][j] = prefixSums[prefixSums.length - 1] - prefixSums[i];
      } else {
        let best = -Infinity;

        for (let k = 1; k <= 2 * j; k++) {
          best = Math.max(
            best,
            prefixSums[i + k] - prefixSums[i] - dp[i + k][Math.max(j, k)],
          );
        }

        dp[i][j] = best;
      }
    }
  }

  return (dp[0][1] + prefixSums[prefixSums.length - 1]) / 2;
}
// @leet end
