// @leet start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <map>

class Solution {
 public:
  int pathSum(TreeNode* root, int targetSum) {
    std::map<long long, int> prefixMap{{0, 1}};

    return helper(root, 0, targetSum, prefixMap);
  }

  int helper(TreeNode* node, long long currSum, int targetSum,
             std::map<long long, int>& prefixMap) {
    if (!node) {
      return 0;
    }

    currSum += node->val;

    int result = 0;
    const auto desiredPrefix = currSum - targetSum;

    if (prefixMap.contains(desiredPrefix)) {
      result += prefixMap[desiredPrefix];
    }

    prefixMap[currSum]++;

    result += helper(node->left, currSum, targetSum, prefixMap);
    result += helper(node->right, currSum, targetSum, prefixMap);

    prefixMap[currSum]--;

    return result;
  }
};
// @leet end
