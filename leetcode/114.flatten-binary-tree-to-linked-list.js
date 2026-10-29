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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
  let curr = root;

  while (curr) {
    if (curr.left) {
      let leftTail = curr.left;

      while (leftTail.right) {
        leftTail = leftTail.right;
      }

      [curr.left, curr.right, leftTail.right] = [null, curr.left, curr.right];
    }

    curr = curr.right;
  }

  return root;
};
// @leet end
