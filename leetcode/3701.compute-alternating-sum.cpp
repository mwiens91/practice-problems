// @leet start

#include <ranges>
#include <vector>

class Solution {
 public:
  int alternatingSum(std::vector<int>& nums) {
    int total = 0;

    for (auto [i, x] : std::views::enumerate(nums)) {
      total += (i % 2 == 0 ? 1 : -1) * x;
    }

    return total;
  }
};
// @leet end
