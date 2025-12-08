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
#include <queue>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> levelOrder(TreeNode* root) {
    std::vector<std::vector<int>> result;
    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
      const int levelSize = q.size();
      std::vector<int> level;

      for (int _ = 0; _ < levelSize; _++) {
        const auto node = q.front();
        q.pop();

        if (!node) {
          continue;
        }

        level.push_back(node->val);

        q.push(node->left);
        q.push(node->right);
      }

      if (!level.empty()) {
        result.push_back(level);
      }
    }

    return result;
  }
};
// @leet end
