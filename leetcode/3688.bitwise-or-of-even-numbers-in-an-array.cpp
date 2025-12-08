// @leet start
#include <vector>

class Solution {
 public:
  int evenNumberBitwiseORs(std::vector<int>& nums) {
    int result = 0;

    for (const auto& num : nums) {
      if (num % 2 == 0) {
        result |= num;
      }
    }

    return result;
  }
};
// @leet end
