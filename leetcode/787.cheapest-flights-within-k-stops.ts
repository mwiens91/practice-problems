// @leet start
function findCheapestPrice(
  n: number,
  flights: number[][],
  src: number,
  dst: number,
  k: number,
): number {
  let curr = Array(n + 1).fill(Infinity);
  curr[src] = 0;

  for (let _ = 0; _ <= k; _++) {
    const next = [...curr];

    for (const [parent, child, cost] of flights) {
      next[child] = Math.min(next[child], curr[parent] + cost);
    }

    curr = next;
  }

  return curr[dst] < Infinity ? curr[dst] : -1;
}
// @leet end
