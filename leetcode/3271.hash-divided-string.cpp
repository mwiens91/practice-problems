// @leet start
#include <cstddef>
#include <string>

class Solution {
 public:
  std::string stringHash(std::string s, int k) {
    std::string result;

    for (std::size_t i = 0; i < s.size(); i += k) {
      // Process substring
      int sum = 0;

      for (std::size_t j = 0; j < k; j++) {
        sum += s[i + j] - 'a';
      }

      result += 'a' + (sum % 26);
    }

    return result;
  }
};
// @leet end
