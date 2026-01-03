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

function levelOrder(root: TreeNode | null): number[][] {
  const result: number[][] = [];
  let curr = root ? [root] : [];

  while (curr.length) {
    result.push(curr.map((node) => node.val));
    curr = curr.flatMap((node) =>
      [node.left, node.right].filter((child) => child !== null),
    );
  }

  return result;
}
// @leet end
