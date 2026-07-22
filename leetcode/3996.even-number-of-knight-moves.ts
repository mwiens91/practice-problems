// @leet start
function canReach(start: number[], target: number[]): boolean {
  return (
    [0, 1].reduce((prev, i) => prev + Math.abs(start[i] - target[i]), 0) % 2 ===
    0
  );
}
// @leet end
