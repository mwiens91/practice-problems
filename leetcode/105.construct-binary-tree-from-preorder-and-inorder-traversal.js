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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  const inorderIdxMap = new Map();

  for (let i = 0; i < inorder.length; i++) {
    inorderIdxMap.set(inorder[i], i);
  }

  const helper = (preLeft, inLeft, size) => {
    if (!size) {
      return null;
    }

    const rootVal = preorder[preLeft];
    const rootInIdx = inorderIdxMap.get(rootVal);

    const leftPreLeftIdx = preLeft + 1;
    const leftInLeftIdx = inLeft;
    const leftSize = rootInIdx - inLeft;

    const rightPreLeftIdx = preLeft + 1 + leftSize;
    const rightInLeftIdx = rootInIdx + 1;
    const rightSize = size - leftSize - 1;

    return new TreeNode(
      rootVal,
      helper(leftPreLeftIdx, leftInLeftIdx, leftSize),
      helper(rightPreLeftIdx, rightInLeftIdx, rightSize),
    );
  };

  return helper(0, 0, preorder.length);
};
// @leet end
