// @leet start
function maxEqualRowsAfterFlips(matrix: number[][]): number {
  const patternFreqs = new Map<BigInt, number>();

  for (const row of matrix) {
    let pattern= 0n;

    for (let i = 1; i < row.length; i++) {
      if (row[i] !== row[i - 1]) {
        pattern |= 1n << BigInt(i);
      }
    }

    patternFreqs.set(pattern, 1 + (patternFreqs.get(pattern) ?? 0));
  }

  return Math.max(...patternFreqs.values());
}
// @leet end
