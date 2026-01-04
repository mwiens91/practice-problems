// @leet start
function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]);

  const result: number[][] = [];

  for (const interval of intervals) {
    if (result.length && result[result.length - 1][1] >= interval[0]) {
      result[result.length - 1][1] = Math.max(
        result[result.length - 1][1],
        interval[1],
      );
    } else {
      result.push(interval);
    }
  }

  return result;
}
// @leet end
