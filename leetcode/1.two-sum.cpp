// @leet start
#include <ranges>
#include <stdexcept>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    // numsMap constains numbers in nums as keys and a corresponding
    // index where a given num has occured as a value
    std::unordered_map<int, int> numsMap;

    for (const auto &[i, x] : std::views::enumerate(nums)) {
      // Check if complement y = target - x exists in numsMap. If it
      // does, we're done.
      const auto y = target - x;

      if (numsMap.contains(y)) {
        return {static_cast<int>(i), numsMap[y]};
      }

      // Insert x into numsMap
      numsMap[x] = i;
    }

    // Since there is a guaranteed solution, we'll never get here
    throw std::runtime_error("solution was not found");
  }
};
// @leet end
