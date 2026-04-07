// @leet start
function countCommas(n: number): number {
  // Relies on n <= 1e5
  return Math.max(n - 999, 0);
};
// @leet end
