// @leet start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let prev = null;
  let curr = slow;

  while (curr) {
    const temp = curr.next;
    curr.next = prev;
    [prev, curr] = [curr, temp];
  }

  let left = head;
  let right = prev;

  while (right !== null && right.next !== null) {
    const tempLeft = left.next;
    const tempRight = right.next;

    left.next = right;
    right.next = tempLeft;

    left = tempLeft;
    right = tempRight;
  }

  return head;
};
// @leet end
