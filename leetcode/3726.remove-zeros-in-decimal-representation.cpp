// @leet start
class Solution {
 public:
  long long removeZeros(long long n) {
    long long result = 0;
    long long baseTenMult = 1;

    while (n > 0) {
      int mod = n % 10;

      if (mod > 0) {
        result += (n % 10) * baseTenMult;
        baseTenMult *= 10;
      }

      n /= 10;
    }

    return result;
  }
};
// @leet end
