// @leet start
function minQueenMoves(source: number[], target: number[]): number {
  const dy = Math.abs(target[0] - source[0]);
  const dx = Math.abs(target[1] - source[1]);

  return !dy && !dx ? 0 : !dy || !dx || dy === dx ? 1 : 2;
}
// @leet end
