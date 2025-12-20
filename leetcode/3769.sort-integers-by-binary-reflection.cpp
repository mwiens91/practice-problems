// @leet start
#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
 public:
  std::vector<int> sortByReflection(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end(), [&](int a, int b) {
      const int revA = binaryReflection(a);
      const int revB = binaryReflection(b);

      if (revA != revB) {
        return revA < revB;
      }

      return a < b;
    });

    return nums;
  }

 private:
  std::unordered_map<int, int> cache;

  int binaryReflection(const int n) {
    if (cache.contains(n)) {
      return cache[n];
    }

    int result = 0;
    int nCopy = n;

    while (nCopy > 0) {
      result <<= 1;
      result |= nCopy & 1;
      nCopy >>= 1;
    }

    cache[n] = result;

    return result;
  }
};
// @leet end
