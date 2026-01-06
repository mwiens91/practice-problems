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

function maxLevelSum(root: TreeNode | null): number {
  let curr = [root];
  let level = 1;
  let max = -Infinity;
  let maxLevel = 1;

  while (curr.length) {
    const next: TreeNode[] = [];
    let sum = 0;

    for (const node of curr) {
      sum += node.val;

      if (node.left) {
        next.push(node.left);
      }

      if (node.right) {
        next.push(node.right);
      }
    }

    if (sum > max) {
      max = sum;
      maxLevel = level;
    }

    curr = next;
    level++;
  }

  return maxLevel;
}
// @leet end
