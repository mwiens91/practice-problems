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
function isBalanced(root: TreeNode | null): boolean {
  return getHeightAndHeightBalance(root)[1];
}

function getHeightAndHeightBalance(root: TreeNode | null): [number, boolean] {
  if (!root) {
    return [-1, true];
  }

  const [leftHeight, leftBalance] = getHeightAndHeightBalance(root.left);
  const [rightHeight, rightBalance] = getHeightAndHeightBalance(root.right);
  const balance =
    leftBalance && rightBalance && Math.abs(leftHeight - rightHeight) <= 1;

  return [1 + Math.max(leftHeight, rightHeight), balance];
}
// @leet end
