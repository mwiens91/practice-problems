// @leet start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestZigZag = function (root) {
  let best = 0;

  const helper = (node, goLeft) => {
    if (!node) {
      return 0;
    }

    const left = helper(node.left, false);
    const right = helper(node.right, true);
    const curr = 1 + (goLeft ? left : right);

    best = Math.max(best, curr);

    return curr;
  };

  helper(root.left, false);
  helper(root.right, true);

  return best;
};
// @leet end
