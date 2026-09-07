// @leet start
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  const ROWS = 9;
  const COLS = 9;

  const isCellValid = (row, col, seen) => {
    const numStr = board[row][col];

    if (numStr === ".") {
      return true;
    }

    const num = Number(numStr);

    if (num < 1 || num > 9 || seen.has(num)) {
      return false;
    }

    seen.add(num);

    return true;
  };

  for (let row = 0; row < ROWS; row++) {
    const seen = new Set();

    for (let col = 0; col < COLS; col++) {
      if (!isCellValid(row, col, seen)) {
        return false;
      }
    }
  }

  for (let col = 0; col < COLS; col++) {
    const seen = new Set();

    for (let row = 0; row < ROWS; row++) {
      if (!isCellValid(row, col, seen)) {
        return false;
      }
    }
  }

  const subBoxValid = (startRow, startCol) => {
    const seen = new Set();

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (!isCellValid(startRow + i, startCol + j, seen)) {
          return false;
        }
      }
    }

    return true;
  };

  // validate the sub-box i sub-boxes from the left and j from the top
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (!subBoxValid(3 * i, 3 * j)) {
        return false;
      }
    }
  }

  return true;
};
// @leet end
