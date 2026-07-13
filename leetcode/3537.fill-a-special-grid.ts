// @leet start
function specialGrid(n: number): number[][] {
  const res = Array.from({ length: 2 ** n }, () =>
    Array.from({ length: 2 ** n }, () => 0),
  );

  const helper = (
    startRange: number,
    size: number,
    startRow: number,
    startCol: number,
  ) => {
    if (size === 1) {
      res[startRow][startCol] = startRange;

      return;
    }

    const half = size / 2;
    const step = size ** 2 / 4;

    helper(startRange, half, startRow, startCol + half);
    helper(startRange + step, half, startRow + half, startCol + half);
    helper(startRange + 2 * step, half, startRow + half, startCol);
    helper(startRange + 3 * step, half, startRow, startCol);
  };

  helper(0, 2 ** n, 0, 0);

  return res;
}
// @leet end
