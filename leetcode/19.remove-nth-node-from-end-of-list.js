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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let len = 0;

  for (let curr = head; curr; curr = curr.next) {
    len++;
  }

  if (len - n === 0) {
    return head.next;
  }

  let curr = head;

  for (let _ = 0; _ < len - n - 1; _++) {
    curr = curr.next;
  }

  curr.next = curr.next.next;

  return head;
};
// @leet end
