// @leet start
#include <vector>

class Solution {
 public:
  int triangularSum(std::vector<int>& nums) {
    for (size_t n = nums.size(); n > 1; n--) {
      for (size_t i = 0; i < n - 1; i++) {
        nums[i] = (nums[i] + nums[i + 1]) % 10;
      }
    }

    return nums[0];
  }
};
// @leet end
