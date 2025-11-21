// @leet start
#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
 public:
  std::vector<int> findMissingElements(std::vector<int>& nums) {
    const std::unordered_set<int> numsSet(nums.begin(), nums.end());
    const int maxNum = *std::max_element(nums.begin(), nums.end());
    const int minNum = *std::min_element(nums.begin(), nums.end());

    std::vector<int> missingElements;

    for (int i = minNum + 1; i < maxNum; i++) {
      if (!numsSet.contains(i)) {
        missingElements.push_back(i);
      }
    }

    return missingElements;
  }
};
// @leet end
