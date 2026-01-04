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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  const valInorderIdx = new Map(inorder.map((v, i) => [v, i]));

  const makeTree = (
    preLeftIdx: number,
    preRightIdx: number,
    inLeftIdx: number,
    inRightIdx: number,
  ): TreeNode | null => {
    if (preLeftIdx > preRightIdx) {
      return null;
    }

    const inRootIdx = valInorderIdx.get(preorder[preLeftIdx])!;
    const leftTreeSize = inRootIdx - inLeftIdx;

    return new TreeNode(
      preorder[preLeftIdx],
      makeTree(
        preLeftIdx + 1,
        preLeftIdx + leftTreeSize,
        inLeftIdx,
        inRootIdx - 1,
      ),
      makeTree(
        preLeftIdx + leftTreeSize + 1,
        preRightIdx,
        inRootIdx + 1,
        inRightIdx,
      ),
    );
  };

  return makeTree(0, preorder.length - 1, 0, inorder.length - 1);
}
// @leet end
