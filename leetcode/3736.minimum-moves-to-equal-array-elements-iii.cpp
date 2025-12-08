// @leet start
#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
 public:
  int minMoves(std::vector<int>& nums) {
    const int maxVal = *std::max_element(nums.begin(), nums.end());

    return maxVal * nums.size() - std::accumulate(nums.begin(), nums.end(), 0);
  }
};
// @leet end
