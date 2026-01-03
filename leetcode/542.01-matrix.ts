// @leet start
function updateMatrix(mat: number[][]): number[][] {
  // Go left to right top to bottom finding the heights, then update
  // again going the other direction
  const rows = mat.length;
  const cols = mat[0].length;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (mat[row][col] !== 0) {
        mat[row][col] =
          1 +
          Math.min(
            row > 0 ? mat[row - 1][col] : Infinity,
            col > 0 ? mat[row][col - 1] : Infinity,
          );
      }
    }
  }

  for (let row = rows - 1; row >= 0; row--) {
    for (let col = cols - 1; col >= 0; col--) {
      if (mat[row][col] !== 0) {
        mat[row][col] = Math.min(
          mat[row][col],
          1 +
            Math.min(
              row < rows - 1 ? mat[row + 1][col] : Infinity,
              col < cols - 1 ? mat[row][col + 1] : Infinity,
            ),
        );
      }
    }
  }

  return mat;
}
// @leet end

