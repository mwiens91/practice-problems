// @leet start
#include <ranges>
#include <set>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> threeSum(std::vector<int> &nums) {
    // Put our input numbers in a map. Frequency map has numbers as keys and
    // their frequency as values.
    std::unordered_map<int, int> freqMap;

    for (const auto &x : nums) {
      if (freqMap.contains(x)) {
        ++freqMap[x];
      } else {
        freqMap[x] = 1;
      }
    }

    // Put all the keys in a vector to iterate over
    std::vector<int> uniqueNums;
    uniqueNums.reserve(freqMap.size());

    for (const auto &x : std::views::keys(freqMap)) {
      uniqueNums.push_back(x);
    }

    // We'll use this to keep track of numbers we've seen so far as we
    // iterate through. This will be used in the third chunk of the main
    // loop below.
    std::set<int> numsSeen;

    // Find all possible solutions
    std::vector<std::vector<int>> results;

    for (const auto &[i, x] : std::views::enumerate(uniqueNums)) {
      // Mark that we've seen x for future iterations
      numsSeen.insert(x);

      // Test for solutions containing exactly three 'x's, which happens
      // only when x == 0
      if (x == 0 && freqMap[x] >= 3) {
        results.push_back({x, x, x});
      }

      // Test for solutions containing exactly two 'x's
      if (freqMap[x] >= 2) {
        // Get complement z
        const auto z = -2 * x;

        if (freqMap.contains(z) && z != 0) {
          results.push_back({x, x, z});
        }
      }

      // Test for solutions containing exactly one 'x' using numbers we
      // haven't iterated over yet. We'll defer handling solutions
      // {x, y, z} with y == z for other iterations of this loop using
      // the block above for handling exactly two of a given number.
      for (const auto &[j, y] :
           std::views::enumerate(uniqueNums | std::views::drop(i + 1))) {
        // Get complement z
        const auto z = -x - y;

        // Make sure we don't have two 'x's or 'y's
        if (x == z || y == z) {
          continue;
        }

        if (numsSeen.contains(z)) {
          results.push_back({x, y, z});
        }
      }
    }

    return results;
  }
};
// @leet end
