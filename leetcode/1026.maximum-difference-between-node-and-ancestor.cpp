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
#include <algorithm>

class Solution {
 public:
  int maxAncestorDiff(TreeNode* root) {
    return std::max(getMaxDifference(root->left, root->val, root->val),
                    getMaxDifference(root->right, root->val, root->val));
  }

 private:
  int getMaxDifference(TreeNode* node, int ancestorMin, int ancestorMax) {
    if (!node) {
      return 0;
    }

    int newMin = std::min(node->val, ancestorMin);
    int newMax = std::max(node->val, ancestorMax);

    return std::max({
        std::abs(node->val - ancestorMin),  // candidates for current node
        std::abs(node->val - ancestorMax),
        getMaxDifference(node->left, newMin, newMax),  // max from left
        getMaxDifference(node->right, newMin, newMax)  // max from right
    });
  };
};
// @leet end
