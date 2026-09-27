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
 * @return {number[]}
 */
var rightSideView = function (root) {
  const result = [];
  let prev = root ? [root] : [];

  while (prev.length) {
    result.push(prev[prev.length - 1].val);
    const curr = [];

    for (const node of prev) {
      if (node.left) {
        curr.push(node.left);
      }

      if (node.right) {
        curr.push(node.right);
      }
    }

    prev = curr;
  }

  return result;
};
// @leet end
