// @leet start
#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
 public:
  int absDifference(std::vector<int>& nums, int k) {
    std::nth_element(nums.begin(), nums.begin() + k, nums.end());
    int minsSum= std::accumulate(nums.begin(), nums.begin() + k, 0);

    std::nth_element(nums.begin(), nums.end() - k, nums.end());
    int maxesSum = std::accumulate(nums.end() - k, nums.end(), 0);

    return maxesSum - minsSum;
  }
};
// @leet end
