// @leet start
#include <algorithm>
#include <limits>
#include <vector>

class Solution {
 public:
  int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
    // Sort by ascending end time
    std::sort(intervals.begin(), intervals.end(),
              [](const auto& a, const auto& b) { return a[1] < b[1]; });

    int currentEnd = std::numeric_limits<int>::min();
    int numRemoved = 0;

    for (const auto& interval : intervals) {
      if (interval[0] >= currentEnd) {
        currentEnd = interval[1];
      } else {
        numRemoved++;
      }
    }

    return numRemoved;
  }
};
// @leet end
