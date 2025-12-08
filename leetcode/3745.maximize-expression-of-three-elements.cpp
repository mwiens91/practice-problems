// @leet start
#include <algorithm>
#include <functional>
#include <vector>

class Solution {
 public:
  int maximizeExpressionOfThree(std::vector<int>& nums) {
    std::nth_element(nums.begin(), nums.begin() + 1, nums.end(), std::greater<int>());

    return nums[0] + nums[1] - *std::min_element(nums.begin(), nums.end());
  }
};
// @leet end
