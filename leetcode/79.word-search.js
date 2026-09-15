// @leet start
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const DIRS = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
  ];
  const MARK = "$";

  // We call helper when we've already matched the character; idx points
  // to the NEXT word index we need to match. Returns true if word is
  // possible from index with current board mark state.
  const helper = (i, j, idx) => {
    if (idx === word.length) {
      return true;
    }

    const old = board[i][j];
    board[i][j] = MARK;

    for (const [di, dj] of DIRS) {
      const newI = i + di;
      const newJ = j + dj;

      if (
        newI >= 0 &&
        newI < board.length &&
        newJ >= 0 &&
        newJ < board[0].length &&
        board[newI][newJ] === word[idx] &&
        helper(newI, newJ, idx + 1)
      ) {
        return true;
      }
    }

    board[i][j] = old;

    return false;
  };

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] === word[0] && helper(i, j, 1)) {
        return true;
      }
    }
  }

  return false;
};
// @leet end
