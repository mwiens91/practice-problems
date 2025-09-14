// @leet start
#include <algorithm>
#include <limits>
#include <vector>

class Solution {
 public:
  int earliestTime(std::vector<std::vector<int>>& tasks) {
    auto result = std::numeric_limits<int>::max();

    for (const auto& task : tasks) {
      result = std::min(result, task[0] + task[1]);
    }

    return result;
  }
};
// @leet end
