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
var goodNodes = function (root) {
  const helper = (node, maxSeen) => {
    if (!node) {
      return 0;
    }

    const nextMaxSeen = Math.max(maxSeen, node.val);

    return (
      Number(node.val >= maxSeen) +
      helper(node.left, nextMaxSeen) +
      helper(node.right, nextMaxSeen)
    );
  };

  return helper(root, -Infinity);
};
// @leet end
