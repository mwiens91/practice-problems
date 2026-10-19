// @leet start
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  let slow = head?.next;
  let fast = head?.next?.next;

  while (fast && fast !== slow) {
    slow = slow.next;
    fast = fast.next?.next;
  }

  if (!fast || !fast.next) {
    return null;
  }

  let entrance = head;

  while (entrance !== slow) {
    entrance = entrance.next;
    slow = slow.next;
  }

  return entrance;
};
// @leet end
