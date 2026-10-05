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

function pathSum(root: TreeNode | null, targetSum: number): number {
  const stack: number[] = [];
  let result = 0;

  const helper = (node: TreeNode | null) => {
    if (!node) {
      return;
    }

    for (let i = 0; i < stack.length; i++) {
      stack[i] += node.val;

      if (stack[i] === targetSum) {
        result++;
      }
    }

    stack.push(node.val);

    if (node.val === targetSum) {
      result++;
    }

    helper(node.left);
    helper(node.right);

    stack.pop();

    for (let i = 0; i < stack.length; i++) {
      stack[i] -= node.val;
    }
  };

  helper(root);

  return result;
}
// @leet end
