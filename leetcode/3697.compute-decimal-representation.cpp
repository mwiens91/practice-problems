// @leet start
#include <algorithm>
#include <vector>

class Solution {
 public:
  std::vector<int> decimalRepresentation(int n) {
    // Store the values in reverse order; we'll reverse everything
    // before returning
    std::vector<int> result;
    long baseTenMult = 1;

    while (n > 0) {
      const int mod = n % 10;

      if (mod != 0) {
        result.push_back(mod * baseTenMult);
      }

      n /= 10;
      baseTenMult *= 10;
    }

    std::reverse(result.begin(), result.end());

    return result;
  }
};
// @leet end
