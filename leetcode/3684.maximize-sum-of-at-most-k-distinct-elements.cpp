// @leet start
#include <algorithm>
#include <functional>
#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
 public:
  std::vector<int> maxKDistinct(std::vector<int>& nums, int k) {
    std::unordered_set<int> seen;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    for (auto num : nums) {
      // Only use each number once
      if (seen.count(num)) {
        continue;
      }

      seen.insert(num);

      // Maintain k largest elements in heap
      if (minHeap.size() < k) {
        minHeap.push(num);
      } else if (num > minHeap.top()) {
        minHeap.pop();
        minHeap.push(num);
      }
    }

    std::vector<int> result;
    result.reserve(minHeap.size());

    while (!minHeap.empty()) {
      result.push_back(minHeap.top());
      minHeap.pop();
    }

    std::reverse(result.begin(), result.end());

    return result;
  }
};
// @leet end
