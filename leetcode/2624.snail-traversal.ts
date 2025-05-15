interface Array<T> {
  snail(rowsCount: number, colsCount: number): T[][];
}

Array.prototype.snail = function <T>(
  this: T[],
  rowsCount: number,
  colsCount: number,
): T[][] {
  // Ensure input is valid
  if (rowsCount * colsCount !== this.length) {
    return [];
  }

  const result: T[][] = [];

  for (let i = 0; i < rowsCount; ++i) {
    result.push([]);

    for (let j = 0; j < colsCount; ++j) {
      // The formulas here I just figured out from inspection
      if (j % 2 === 0) {
        result[i].push(this[j * rowsCount + i]);
      } else {
        result[i].push(this[(j + 1) * rowsCount - 1 - i]);
      }
    }
  }

  return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
