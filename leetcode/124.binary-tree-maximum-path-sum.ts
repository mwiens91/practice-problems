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

function maxPathSum(root: TreeNode | null): number {
  let best = root.val;

  const helper = (node) => {
    if (node === null) {
      return 0;
    }

    const bestLeft = helper(node.left);
    const bestRight = helper(node.right);

    best = Math.max(best, node.val + bestLeft + bestRight);

    return Math.max(0, node.val + Math.max(bestLeft, bestRight));
  };

  helper(root);

  return best;
}
// @leet end
