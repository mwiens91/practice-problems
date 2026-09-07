// @leet start
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => a[1] - b[1]);

  let numSkipped = 0;
  let currEnd = -Infinity;

  for (const [start, end] of intervals) {
    if (start < currEnd) {
      numSkipped++;
    } else {
      currEnd = end;
    }
  }

  return numSkipped;
};
// @leet end
