// @leet start
#include <algorithm>
#include <ranges>
#include <string>
#include <unordered_map>

class Solution {
 public:
  std::string majorityFrequencyGroup(std::string s) {
    // Get character counts
    std::unordered_map<char, int> counts;

    for (char c : s) {
      counts[c] += 1;
    }

    // Find the count that has the most characters. Break ties with
    // larger count.
    std::unordered_map<int, int> numCharsPerCount;

    for (int count : counts | std::views::values) {
      numCharsPerCount[count] += 1;
    }

    int countWithMost = 0;
    int mostNumChars = 0;

    for (auto [count, numChars] : numCharsPerCount) {
      if (numChars > mostNumChars) {
        countWithMost = count;
        mostNumChars = numChars;
      } else if (numChars == mostNumChars && count > countWithMost) {
        countWithMost = count;
      }
    }

    // Aggregate characters with the target count
    std::string result;

    for (auto [c, count] : counts) {
      if (count == countWithMost) {
        result.push_back(c);
      }
    }

    return result;
  }
};
// @leet end
