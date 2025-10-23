// @leet start
#include <unordered_map>
#include <vector>

class Solution {
 public:
  int sumDivisibleByK(std::vector<int>& nums, int k) {
    std::unordered_map<int, int> freqs;

    for (int num : nums) {
      freqs[num] += 1;
    }

    int result = 0;

    for (auto [num, freq] : freqs) {
      if (freq % k == 0) {
        result += num * freq;
      }
    }

    return result;
  }
};
// @leet end
