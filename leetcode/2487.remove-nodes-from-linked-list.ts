// @leet start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNodes(head: ListNode | null): ListNode | null {
  return helper(head)[0];
}

function helper(node: ListNode | null): [ListNode | null, number] {
  if (!node) {
    return [null, -Infinity];
  }

  const [next, max] = helper(node.next);

  if (node.val < max) {
    return [next, max];
  }

  node.next = next;

  return [node, Math.max(max, node.val)];
}
// @leet end
