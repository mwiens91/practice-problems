// @leet start
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    // Put integers into an unordered map such that the key
    // corresponds to the number and the value corresponds to a
    // vector of indices where that number occurs
    unordered_map<int, vector<int>> numsMap;

    for (size_t i = 0, e = nums.size(); i != e; ++i) {
      // The number
      const auto x = nums[i];

      // How we add the index depends on whether this is the first
      // time we've seen x
      if (numsMap.contains(x)) {
        numsMap[x].push_back(i);
      } else {
        numsMap[x] = {static_cast<int>(i)};
      }
    }

    // Go through all integers in nums again, and check to see if
    // the complement y = target - x exists. If it does then the
    // solution is {i, j} where i and j are the indices of x and y.
    // The logic is slightly different for x == y and x != y.
    for (const auto &[x, v] : numsMap) {
      const auto y = target - x;

      // x == y. If we've seen x at least twice, then return two of the
      // indices, otherwise this number isn't going to be part of a
      // solution.
      if (x == y) {
        if (v.size() >= 2) {
          return {v[0], v[1]};
        }

        continue;
      }

      // x != y
      if (numsMap.contains(y)) {
        return {v[0], numsMap[y][0]};
      }
    }

    // Since there is a guaranteed solution, we'll never get here
    return {0};
  }
};
// @leet end
