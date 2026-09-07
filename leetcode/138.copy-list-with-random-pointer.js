// @leet start
/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  const copyMap = new Map();

  const helper = (origNode) => {
    if (origNode === null) {
      return null;
    }

    if (copyMap.has(origNode)) {
      return copyMap.get(origNode);
    }

    const copy = new _Node(origNode.val);
    copyMap.set(origNode, copy);

    copy.next = helper(origNode.next);
    copy.random = helper(origNode.random);

    return copy;
  };

  return helper(head);
};
// @leet end
