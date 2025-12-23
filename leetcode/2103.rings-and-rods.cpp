// @leet start
#include <array>
#include <cstddef>
#include <numeric>
#include <string>
#include <unordered_map>

class Solution {
 public:
  int countPoints(std::string rings) {
    const std::unordered_map<char, std::size_t> colorToIdx = {{'R', 0}, {'G', 1}, {'B', 2}};
    std::array<std::array<bool, 3>, 10> ringHasColors;

    for (std::size_t i = 0; i < rings.size(); i += 2) {
      ringHasColors[rings[i + 1] - '0'][colorToIdx.at(rings[i])] = true;
    }

    return std::accumulate(ringHasColors.begin(), ringHasColors.end(), 0,
                           [](auto accum, const auto& inner) {
                             const int numColors = std::accumulate(inner.begin(), inner.end(), 0);
                             return accum + (numColors == 3);
                           });
  }
};
// @leet end
