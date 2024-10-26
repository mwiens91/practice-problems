// @leet start
#include <algorithm>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> threeSum(std::vector<int> &nums) {
    // Hold the solutions
    std::vector<std::vector<int>> results;

    // Sort the input
    std::sort(nums.begin(), nums.end());

    // The idea here is similar to two-sum ii (problem 167). Here we'll
    // fix an i, and let its negative be the desired target, and then
    // run something similar to two-pointer solution to two-sum ii.
    for (size_t i = 0; i < nums.size() - 2; i++) {
      // Make sure we don't do-over a duplicate value
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      const auto x = nums[i];

      // The following is basically two-sum ii except we're gathering
      // *all* solutions, not just one. See two-sum ii solution for
      // comments on the following code.
      size_t j = i + 1;
      size_t k = nums.size() - 1;

      for (; j < k; ++j) {
        if (j > i + 1 && nums[j] == nums[j - 1]) {
          continue;
        }

        const auto y = nums[j];
        const auto complement = -x - y;

        for (; j < k ; --k) {
          const auto z = nums[k];

          if (z == complement) {
            results.push_back({x, y, z});
            break;
          } else if (z < complement) {
            break;
          }
        }
      }
    }

    return results;
  }
};
// @leet end
