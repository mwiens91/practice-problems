// @leet start
#include <vector>
class Solution {
 public:
  long long sumAndMultiply(int n) {
    long nonZeroNum = 0;
    int nonZeroSum = 0;
    long baseTenMult = 1;

    while (n > 0) {
      const int mod = n % 10;

      if (mod != 0) {
        nonZeroNum += mod * baseTenMult;
        nonZeroSum += mod;
        baseTenMult *= 10;
      }

      n /= 10;
    }

    return nonZeroNum * nonZeroSum;
  }
};
// @leet end
