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
function invertTree(root: TreeNode | null): TreeNode | null {
  const stack = [root];

  while (stack.length) {
    const node = stack.pop();

    if (node) {
      [node.left, node.right] = [node.right, node.left];
      stack.push(node.right, node.left);
    }
  }

  return root;
}
// @leet end

