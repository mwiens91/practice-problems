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

    // Find all possible solutions. Using a set to store solutions
    // because with the current implementation we'll be adding most
    // results twice; it's not hard to implement this so each result is
    // added exactly once, but I don't think that really gains much
    // (could actually be less efficient?).
    std::set<std::tuple<int, int, int>> results;

    for (const auto &[i, x] : std::views::enumerate(uniqueNums)) {
      // Test for solutions containing three 'x's, which happens only
      // when x == 0. We continue here because there are no solutions
      // with two '0's, and solutions with one '0' will be picked up
      // with other iterations of this loop; also if we know x != 0
      // below we can simplify logic greatly.
      if (x == 0) {
        if (freqMap[x] >= 3) {
          results.insert({x, x, x});
        }

        continue;
      }

      // Test for solutions containing exactly two 'x's
      if (freqMap[x] >= 2) {
        // Get complement z (!= x)
        const auto z = -2 * x;

        if (freqMap.contains(z)) {
          results.insert(makeSortedThreeTuple(x, x, z));
        }
      }

      // Test for solutions containing exactly one 'x'. We'll defer
      // handling solutions {x, y, z} with y == z for other iterations
      // of this loop using the block above for handling two of a given
      // number, which lets us simply some logic here.
      for (const auto &[j, y] :
           std::views::enumerate(uniqueNums | std::views::drop(i + 1))) {
        // Get the complement z we need to find
        const auto z = -x - y;

        // Make sure numbers are unique
        if (x == z || y == z) {
          continue;
        }

        if (freqMap.contains(z)) {
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
