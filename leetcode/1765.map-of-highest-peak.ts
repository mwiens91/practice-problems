// @leet start
function highestPeak(isWater: number[][]): number[][] {
  // We'll put all heights into isWater. The name doesn't really make
  // sense but doing this saves memory. Note that this solution is
  // basically the same as 542, with a small modification.
  const rows = isWater.length;
  const cols = isWater[0].length;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (isWater[row][col] === 1) {
        isWater[row][col] = 0;
      } else {
        isWater[row][col] =
          1 +
          Math.min(
            row > 0 ? isWater[row - 1][col] : Infinity,
            col > 0 ? isWater[row][col - 1] : Infinity,
          );
      }
    }
  }

  for (let row = rows - 1; row >= 0; row--) {
    for (let col = cols - 1; col >= 0; col--) {
      if (isWater[row][col] !== 0) {
        isWater[row][col] = Math.min(
          isWater[row][col],
          1 +
            Math.min(
              row < rows - 1 ? isWater[row + 1][col] : Infinity,
              col < cols - 1 ? isWater[row][col + 1] : Infinity,
            ),
        );
      }
    }
  }

  return isWater;
}
// @leet end
