// @leet start
#include <algorithm>
#include <ranges>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>

// Convenience function we'll use later
std::tuple<int, int, int> makeSortedThreeTuple(int x, int y, int z) {
  if (x > y) {
    std::swap(x, y);
  }

  if (y > z) {
    std::swap(y, z);
  }

  if (x > y) {
    std::swap(x, y);
  }

  return {x, y, z};
}

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

    // Put all the keys in a vector
    std::vector<int> uniqueNums;
    uniqueNums.reserve(freqMap.size());

    for (const auto &x : std::views::keys(freqMap)) {
      uniqueNums.push_back(x);
    }

    // Go through each possible two-sum x + y and check if there's a
    // third number z = -x - y that makes the sum 0. Using a set to
    // store solutions because with the current implementation we'll be
    // adding most results twice; it's not hard to implement this so
    // each result is added exactly once, but I don't think that really
    // gains much (could actually be less efficient?).
    std::set<std::tuple<int, int, int>> results;

    for (size_t i = 0; i < uniqueNums.size(); ++i) {
      // Get a number x
      const auto x = uniqueNums[i];

      // We'll handle x == 0 separately here. We won't do other
      // processing because all other solutions containing zero will be
      // handled when we iterate over the other numbers.
      if (x == 0) {
        if (freqMap[x] > 2) {
          results.insert({x, x, x});
        }

        continue;
      }

      // Test for possible solution containing 2 'x's
      if (freqMap[x] > 1) {
        // Get complement z
        const auto z = -2 * x;

        if (freqMap.contains(z)) {
          results.insert(makeSortedThreeTuple(x, x, z));
        }
      }

      // Now iterate through all other pairs to find solutions with
      // unique numbers (explained below)
      for (size_t j = i + 1; j < uniqueNums.size(); ++j) {
        // Get another number y and the complement z we need to find
        const auto y = uniqueNums[j];
        const auto z = -x - y;

        // If x == z we've already handled this case above. If y == z we'll deal
        // with this case when the outer loop i index is equal to the current j
        // index.
        if (x != z && y != z && freqMap.contains(z)) {
          results.insert(makeSortedThreeTuple(x, y, z));
        }
      }
    }

    // Convert results set of tuples to a vector of vectors
    std::vector<std::vector<int>> resultsVec;
    resultsVec.reserve(results.size());

    for (const auto &result : results) {
      resultsVec.push_back(
          {std::get<0>(result), std::get<1>(result), std::get<2>(result)});
    }

    return resultsVec;
  }
};
// @leet end
