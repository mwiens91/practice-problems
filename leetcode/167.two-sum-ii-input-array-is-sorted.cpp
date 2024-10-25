// @leet start
#include <stdexcept>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &numbers, int target) {
    // Go through numbers from front to back using a forward and
    // backward pointer
    size_t i = 0;
    size_t j = numbers.size() - 1;

    for (;; ++i) {
      // Get lower number x and complement y = target - x
      const auto x = numbers[i];
      const auto y = target - x;

      // Go through upper numbers z until we find the complement y or we
      // reach numbers which imply the complement does not exist for
      // this x
      for (;; --j) {
        // Upper number z
        const auto z = numbers[j];

        if (z == y) {
          // Found solution. Recall numbers on paper are 1-indexed
          return {static_cast<int>(i) + 1, static_cast<int>(j) + 1};
        } else if (z < y) {
          // Complement does not exist
          break;
        }
      }
    }

    // Since there is a guaranteed solution, we'll never get here
    throw std::runtime_error("solution was not found");
  }
};
// @leet end
