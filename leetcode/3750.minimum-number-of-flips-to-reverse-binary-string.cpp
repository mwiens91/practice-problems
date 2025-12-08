// @leet start
#include <bit>

class Solution {
 public:
  int minimumFlips(int n) {
    int diffs = 0;
    int left = std::bit_width(static_cast<unsigned>(n)) - 1;
    int right = 0;

    while (left > right) {
      if (((n >> left) & 1) != ((n >> right) & 1)) {
        diffs++;
      }

      left--;
      right++;
    }

    return 2 * diffs;
  }
};
// @leet end
