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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const res = []; // number[][]
  let currLevel = [root];

  while (currLevel.length) {
    const currLevelVals = []; // number[]
    const nextLevel = []; // (TreeNode || null)[]

    for (const node of currLevel) {
      if (node === null) {
        continue;
      }

      currLevelVals.push(node.val);
      nextLevel.push(node.left);
      nextLevel.push(node.right);
    }

    if (currLevelVals.length) {
      res.push(currLevelVals);
    }

    currLevel = nextLevel;
  }

  return res;
};
// @leet end
