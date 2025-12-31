// @leet start
function garbageCollection(garbage: string[], travel: number[]): number {
  const prefixSums = travel.reduce(
    (acc, curr) => {
      acc.push(acc[acc.length - 1] + curr);
      return acc;
    },
    [0],
  );
  const seen: Set<string> = new Set();
  let result = 0;

  for (let i = garbage.length - 1; i >= 0; i--) {
    result += garbage[i].length;
    [...new Set(garbage[i])].forEach((type) => {
      if (!seen.has(type)) {
        seen.add(type);
        result += prefixSums[i];
      }
    });
  }

  return result;
}
// @leet end
