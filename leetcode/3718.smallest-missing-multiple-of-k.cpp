// @leet start
#include <unordered_set>
#include <vector>

class Solution {
 public:
  int missingMultiple(std::vector<int>& nums, int k) {
    const std::unordered_set<int> numsSet(nums.begin(), nums.end());

    for (int i = 1;; i++) {
      const auto num = i * k;

      if (!numsSet.contains(num)) {
        return num;
      }
    }
  }
};
// @leet end
