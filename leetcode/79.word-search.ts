// @leet start
function exist(board: string[][], word: string): boolean {
  const rows = board.length;
  const cols = board[0].length;

  // Get out early if there aren't enough letters on the board to form
  // the word
  const boardCounts = new Map<string, number>();
  const wordCounts = new Map<string, number>();

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      boardCounts.set(
        board[row][col],
        1 + (boardCounts.get(board[row][col]) ?? 0),
      );
    }
  }

  for (const c of word) {
    wordCounts.set(c, 1 + (wordCounts.get(c) ?? 0));
  }

  for (const [k, count] of wordCounts.entries()) {
    if (!boardCounts.has(k) || boardCounts.get(k)! < count) {
      return false;
    }
  }

  // General solution
  const backtrack = (i: number, row: number, col: number): boolean => {
    if (i === word.length) {
      return true;
    }

    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      board[row][col] !== word[i]
    ) {
      return false;
    }

    // Mark as visited
    const val = board[row][col];
    board[row][col] = "#";

    for (const [newRow, newCol] of [
      [row - 1, col],
      [row + 1, col],
      [row, col - 1],
      [row, col + 1],
    ]) {
      if (backtrack(i + 1, newRow, newCol)) {
        return true;
      }
    }

    board[row][col] = val;

    return false;
  };

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (backtrack(0, row, col)) {
        return true;
      }
    }
  }

  return false;
}
// @leet end
