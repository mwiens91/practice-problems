// @leet start
#include <string>
#include <unordered_set>

class Solution {
 public:
  int maxDistinct(std::string s) { return std::unordered_set<char>(s.begin(), s.end()).size(); }
};
// @leet end
