// @leet start
#include <string>

class Solution {
 public:
  bool scoreBalance(std::string s) {
    int leftNext = 0;
    int rightNext = s.size() - 1;

    int leftScore = 0;
    int rightScore = 0;

    while (leftNext <= rightNext) {
      if (leftScore <= rightScore) {
        leftScore += s[leftNext] -  'a' + 1;
        leftNext++;
      } else {
        rightScore += s[rightNext] - 'a' + 1;
        rightNext--;
      }
    }

    return leftScore == rightScore;
  }
};
// @leet end
