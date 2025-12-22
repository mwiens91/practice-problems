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
#include <vector>

class Solution {
 public:
  std::vector<TreeNode*> allPossibleFBT(int n) {
    std::vector<std::vector<TreeNode*>> dp(n + 1);
    dp[1].push_back(new TreeNode{});

    for (int i = 3; i <= n; i += 2) {
      for (int nLeft = 1; nLeft < i; nLeft += 2) {
        const int nRight = i - nLeft - 1;

        for (const auto& left : dp[nLeft]) {
          for (const auto& right : dp[nRight]) {
            dp[i].push_back(new TreeNode{0, left, right});
          }
        }
      }
    }

    return dp[n];
  }
};
// @leet end
