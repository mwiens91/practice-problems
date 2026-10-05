// @leet start
#include <cmath>
#include <vector>

class Solution {
 public:
  int findTargetSumWays(vector<int>& nums, int target) {
    int totalSum = 0;

    for (int num : nums) {
      totalSum += num;
    }

    if (std::abs(target) > totalSum || (totalSum - target) % 2 != 0) {
      return 0;
    }

    // Find number of subsets equalling (totalSum - target) / 2
    const int targetSum = (totalSum - target) / 2;
    std::vector<int> counts(targetSum + 1, 0);
    counts[0] = 1;

    for (int num : nums) {
      for (int i = targetSum; i >= num; i--) {
        counts[i] += counts[i - num];
      }
    }

    return counts[targetSum];
  }
};
// @leet end
