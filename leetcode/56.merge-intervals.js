// @leet start
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((y1, y2) => {
    if (y1[0] !== y2[0]) {
      return y1[0] - y2[0];
    }

    return y1[1] - y2[1];
  });

  const result = [];
  let currStart = intervals[0][0];
  let currEnd = intervals[0][1];

  for (const [start, end] of intervals) {
    if (start <= currEnd) {
      currEnd = Math.max(currEnd, end);
    } else {
      result.push([currStart, currEnd]);
      currStart = start;
      currEnd = end;
    }
  }

  result.push([currStart, currEnd]);

  return result;
};
// @leet end
