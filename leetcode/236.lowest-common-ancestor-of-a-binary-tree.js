// @leet start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  const helper = (node) => {
    if (node === null || node === p || node === q) {
      return node;
    }

    const left = helper(node.left);
    const right = helper(node.right);

    return left !== null && right !== null ? node : (left ?? right);
  };

  return helper(root);
};
// @leet end
