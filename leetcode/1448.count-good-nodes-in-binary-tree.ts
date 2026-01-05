// @leet start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function goodNodes(root: TreeNode | null): number {
  return helper(root, root.val);
}

function helper(node: TreeNode | null, max: number): number {
  if (!node) {
    return 0;
  }

  const newMax = Math.max(max, node.val);

  return (
    (node.val >= max ? 1 : 0) +
    helper(node.left, newMax) +
    helper(node.right, newMax)
  );
}
// @leet end
