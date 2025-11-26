// @leet start
#include <algorithm>
#include <cmath>
#include <limits>
#include <unordered_map>
#include <vector>

class Solution {
 public:
  int minimumDistance(std::vector<int>& nums) {
    // Setup map with num -> idxs
    std::unordered_map<int, std::vector<int>> numIdxs;

    // NOTE: using int instead of size_t here will be useful for later
    for (int i = 0; i < nums.size(); i++) {
      numIdxs[nums[i]].push_back(i);
    }

    // Calculate min distance
    // NOTE : treating max int as infinity okay given constraints
    int minDistance = std::numeric_limits<int>::max();

    for (const auto& [_, idxs] : numIdxs) {
      for (size_t j = 2; j < idxs.size(); j++) {
        int distance = std::abs(idxs[j - 2] - idxs[j - 1]) + std::abs(idxs[j - 1] - idxs[j]) +
                       std::abs(idxs[j] - idxs[j - 2]);

        minDistance = std::min(minDistance, distance);
      }
    }

    return minDistance != std::numeric_limits<int>::max() ? minDistance : -1;
  }
};
// @leet end
