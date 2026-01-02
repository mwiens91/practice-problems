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
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null,
): TreeNode | null {
  if (!root || !p || !q) {
    throw new Error();
  }

  const [lo, hi] = p.val <= q.val ? [p.val, q.val] : [q.val, p.val];
  let curr = root;

  while (curr.val < lo || curr.val > hi) {
    curr = curr.val < lo ? curr.right! : curr.left!;
  }

  return curr;
}
// @leet end
