// @leet start
function maximumCostSubstring(
  s: string,
  chars: string,
  vals: number[],
): number {
  const costs = Object.assign(
    Object.fromEntries(
      [...new Array(26).keys()].map((i) => [
        String.fromCharCode("a".charCodeAt(0) + i),
        i + 1,
      ]),
    ),
    Object.fromEntries([...chars].map((c, i) => [c, vals[i]])),
  );

  let max = 0;
  let curr = 0;

  for (const c of s) {
    curr = curr + costs[c] > 0 ? curr + costs[c] : 0;
    max = Math.max(max, curr);
  }

  return max;
}
// @leet end
