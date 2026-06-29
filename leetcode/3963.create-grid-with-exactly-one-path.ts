// @leet start
function createGrid(m: number, n: number): string[] {
  return Array.from({ length: m }, (_, r) =>
    Array.from({ length: n }, (_, c) =>
      r === 0 || c === n - 1 ? "." : "#",
    ).join(""),
  );
}
// @leet end
