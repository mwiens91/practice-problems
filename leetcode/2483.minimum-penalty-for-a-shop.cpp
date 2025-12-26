// @leet start
#include <algorithm>
#include <numeric>
#include <ranges>
#include <string>

class Solution {
 public:
  int bestClosingTime(std::string customers) {
    int penalty = std::accumulate(customers.begin(), customers.end(), 0,
                                  [](int accum, char c) { return accum + (c == 'Y' ? 1 : 0); });
    int minHour = 0;
    int minPenalty = penalty;

    for (auto [i, c] : std::views::enumerate(customers)) {
      if (c == 'Y') {
        penalty -= 1;

        if (penalty < minPenalty) {
          minHour = i + 1;
          minPenalty = penalty;
        }
      } else {
        // c == 'N'
        penalty += 1;
      }
    }

    return minHour;
  }
};
// @leet end
