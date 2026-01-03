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

function diameterOfBinaryTree(root: TreeNode | null): number {
  return getHeightAndDiam(root)[1];
}

function getHeightAndDiam(root: TreeNode | null): [number, number] {
  if (!root) {
    return [-1, 0];
  }

  const [leftHeight, leftDiam] = getHeightAndDiam(root.left);
  const [rightHeight, rightDiam] = getHeightAndDiam(root.right);
  const maxDiam = Math.max(2 + leftHeight + rightHeight, leftDiam, rightDiam);

  return [1 + Math.max(leftHeight, rightHeight), maxDiam];
}
// @leet end
