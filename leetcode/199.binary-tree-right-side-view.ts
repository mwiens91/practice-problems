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

function rightSideView(root: TreeNode | null): number[] {
  const result: number[] = [];
  let curr: TreeNode[] = root ? [root] : [];

  while (curr.length) {
    result.push(curr[curr.length - 1].val);

    const next: TreeNode[] = [];

    for (const node of curr) {
      if (node.left) {
        next.push(node.left);
      }

      if (node.right) {
        next.push(node.right);
      }
    }

    curr = next;
  }

  return result;
}
// @leet end
