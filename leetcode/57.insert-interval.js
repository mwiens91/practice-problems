// @leet start
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  let left = 0;
  let right = intervals.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (intervals[mid][1] >= newInterval[0]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  const insertIdx = left;

  // no need to update left
  right = intervals.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (intervals[mid][0] > newInterval[1]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  const mergeToIdx = left - 1;

  const mergedInterval =
    insertIdx <= mergeToIdx
      ? [
          Math.min(intervals[insertIdx][0], newInterval[0]),
          Math.max(intervals[mergeToIdx][1], newInterval[1]),
        ]
      : newInterval;

  return [
    ...intervals.slice(0, insertIdx),
    mergedInterval,
    ...intervals.slice(mergeToIdx + 1),
  ];
};
// @leet end
