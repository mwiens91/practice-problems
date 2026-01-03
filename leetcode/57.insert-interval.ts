// @leet start
function insert(intervals: number[][], newInterval: number[]): number[][] {
  // Find insertion index into intervals
  let lo = 0;
  let hi = intervals.length - 1;

  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);

    if (intervals[mid][0] < newInterval[0]) {
      lo = mid + 1;
    } else {
      hi = mid - 1;
    }
  }

  // Merge previous and any following intervals together
  let prevIdx = lo - 1;
  let nextIdx = lo;

  if (prevIdx >= 0 && intervals[prevIdx][1] >= newInterval[0]) {
    newInterval[0] = intervals[prevIdx][0];
    newInterval[1] = Math.max(newInterval[1], intervals[prevIdx][1]);
    prevIdx--;
  }

  while (
    nextIdx < intervals.length &&
    intervals[nextIdx][0] <= newInterval[1]
  ) {
    newInterval[1] = Math.max(newInterval[1], intervals[nextIdx][1]);
    nextIdx++;
  }

  return [
    ...intervals.slice(0, prevIdx + 1),
    newInterval,
    ...intervals.slice(nextIdx, intervals.length),
  ];
}
// @leet end
