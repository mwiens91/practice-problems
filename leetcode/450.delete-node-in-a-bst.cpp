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
class Solution {
 public:
  TreeNode* deleteNode(TreeNode* root, int key) {
    // Get a pointer to the pointer to target node
    auto** toDeletePtr = &root;

    for (;;) {
      if (!*toDeletePtr) {
        return root;
      }

      const int currentVal = (*toDeletePtr)->val;

      if (currentVal == key) {
        break;
      }

      if (currentVal > key) {
        toDeletePtr = &((*toDeletePtr)->left);
      } else {
        toDeletePtr = &((*toDeletePtr)->right);
      }
    }

    // Remove the target node
    auto* toDelete = *toDeletePtr;

    if (toDelete->left && toDelete->right) {
      // Find predecessor
      auto** predPtr = &(toDelete->left);

      while ((*predPtr)->right) {
        predPtr = &((*predPtr)->right);
      }

      // Move predecessor into node to delete's position
      auto* pred = *predPtr;
      *predPtr = pred->left;

      pred->left = toDelete->left;
      pred->right = toDelete->right;

      *toDeletePtr = pred;
    } else if (toDelete->left) {
      *toDeletePtr = toDelete->left;
    } else {
      *toDeletePtr = toDelete->right;
    }

    // Free the node and return root of tree
    delete toDelete;

    return root;
  }
};
// @leet end
