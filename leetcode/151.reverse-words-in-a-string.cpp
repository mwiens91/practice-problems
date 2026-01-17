// @leet start
#include <cstddef>
#include <string>

class Solution {
 public:
  std::string reverseWords(std::string s) { return helper(s, 0); }

 private:
  std::string helper(const std::string& s, std::size_t begin) {
    std::size_t i = begin;

    while (i < s.size() && s[i] == ' ') {
      i++;
    }

    if (i >= s.size()) {
      return "";
    }

    const auto start = i;

    while (i < s.size() && s[i] != ' ') {
      i++;
    }

    const auto word = s.substr(start, i - start);
    const auto next = helper(s, i);

    if (next.empty()) {
      return word;
    }

    return next + " " + word;
  }
};
// @leet end
