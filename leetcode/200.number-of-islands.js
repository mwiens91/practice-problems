// @leet start
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const LAND = "1";
  const EXPLORED = "-1";
  const m = grid.length;
  const n = grid[0].length;

  // Explore all adjacent land and mark processed land as water
  const dfs = (startR, startC) => {
    grid[startR][startC] = EXPLORED;
    const stack = [[startR, startC]]; // [number, number][]

    while (stack.length) {
      const [r, c] = stack.pop();

      for (const [dr, dc] of DIRS) {
        const nextR = r + dr;
        const nextC = c + dc;

        if (
          nextR >= 0 &&
          nextR < m &&
          nextC >= 0 &&
          nextC < n &&
          grid[nextR][nextC] === LAND
        ) {
          grid[nextR][nextC] = EXPLORED;
          stack.push([nextR, nextC]);
        }
      }
    }
  };

  let res = 0;

  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === LAND) {
        res++;
        dfs(r, c);
      }
    }
  }

  return res;
};
// @leet end
