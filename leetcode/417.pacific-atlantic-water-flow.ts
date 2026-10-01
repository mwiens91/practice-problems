// @leet start
function pacificAtlantic(heights: number[][]): number[][] {
  const DIRS = [
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 0],
  ];
  const m = heights.length;
  const n = heights[0].length;

  const getReachable = (fromPacific: boolean) => {
    const reachable: boolean[][] = Array.from({ length: m }, () =>
      Array(n).fill(false),
    );
    let curr: [number, number][] = [];

    if (fromPacific) {
      for (let j = 0; j < n; j++) {
        reachable[0][j] = true;
        curr.push([0, j]);
      }

      for (let i = 1; i < m; i++) {
        reachable[i][0] = true;
        curr.push([i, 0]);
      }
    } else {
      for (let j = 0; j < n; j++) {
        reachable[m - 1][j] = true;
        curr.push([m - 1, j]);
      }

      for (let i = 0; i < m - 1; i++) {
        reachable[i][n - 1] = true;
        curr.push([i, n - 1]);
      }
    }

    while (curr.length) {
      const next: [number, number][] = [];

      for (const [i, j] of curr) {
        for (const [di, dj] of DIRS) {
          const adjI = i + di;
          const adjJ = j + dj;

          if (
            adjI >= 0 &&
            adjI < m &&
            adjJ >= 0 &&
            adjJ < n &&
            !reachable[adjI][adjJ] &&
            heights[i][j] <= heights[adjI][adjJ]
          ) {
            reachable[adjI][adjJ] = true;
            next.push([adjI, adjJ]);
          }
        }
      }

      curr = next;
    }

    return reachable;
  };

  const reachesPacific = getReachable(true);
  const reachesAtlantic = getReachable(false);
  const result: [number, number][] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (reachesPacific[i][j] && reachesAtlantic[i][j]) {
        result.push([i, j]);
      }
    }
  }

  return result;
}
// @leet end
