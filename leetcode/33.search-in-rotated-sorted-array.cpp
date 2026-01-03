// @leet start
#include <vector>

class Solution {
 public:
  int search(std::vector<int>& nums, int target) {
    int lo = 0;
    int hi = nums.size() - 1;

    while (lo <= hi) {
      const int mid = (lo + hi) / 2;

      if (nums[mid] == target) {
        return mid;
      }

      if (nums[lo] <= nums[mid]) {
        // Left half sorted
        if (nums[mid] > target && nums[lo] <= target) {
          hi = mid - 1;
        } else {
          lo = mid + 1;
        }
      } else {
        // Right half sorted
        if (nums[mid] < target && nums[hi] >= target) {
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
    }

    return -1;
  }
};
// @leet end
