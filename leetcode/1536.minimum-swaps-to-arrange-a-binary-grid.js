// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minSwaps = function (grid) {
  const getRightMostOneIdx = (row) => {
    for (let i = row.length - 1; i >= 0; i--) {
      if (row[i] === 1) {
        return i;
      }
    }

    return -1;
  };

  const MARK = Infinity;
  const oneIdxs = grid.map(getRightMostOneIdx);

  let i = 0;
  let offset = 0;
  let swaps = 0;

  while (i < oneIdxs.length) {
    if (oneIdxs[i] === MARK) {
      i++;
      offset--;
    } else if (oneIdxs[i] <= i + offset) {
      i++;
    } else {
      let success = false;
      let markedSeen = 0;

      for (let j = i + 1; j < oneIdxs.length; j++) {
        if (oneIdxs[j] === MARK) {
          markedSeen++;
        } else if (oneIdxs[j] <= i + offset) {
          success = true;

          oneIdxs[j] = MARK;
          swaps += j - i - markedSeen;

          offset++;
          break;
        }
      }

      if (!success) {
        return -1;
      }
    }
  }

  return swaps;
};
// @leet end
