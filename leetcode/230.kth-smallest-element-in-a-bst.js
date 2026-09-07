// @leet start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  let currCount = 0;

  const inOrder = (node) => {
    if (node === null) {
      return null;
    }

    const left = inOrder(node.left);

    if (left !== null) {
      return left;
    }

    currCount++;

    if (currCount === k) {
      return node.val;
    }

    return inOrder(node.right);
  };

  return inOrder(root);
};
// @leet end
