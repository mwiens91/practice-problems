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
 * @return {ListNode}
 */
var sortList = function (head) {
  if (!head?.next) {
    return head;
  }

  // Get mid and cut list in two
  let prev = head;
  let mid = head;
  let fast = head;

  while (fast?.next) {
    prev = mid;
    mid = mid.next;
    fast = fast.next.next;
  }

  prev.next = null;

  const left = sortList(head);
  const right = sortList(mid);

  return merge(left, right);
};

// Precondition: left, right !== null
const merge = (left, right) => {
  let head;

  if (left.val <= right.val) {
    head = left;
    left = left.next;
  } else {
    head = right;
    right = right.next;
  }

  let tail = head;

  while (left && right) {
    if (left.val <= right.val) {
      tail.next = left;
      left = left.next;
    } else {
      tail.next = right;
      right = right.next;
    }

    tail = tail.next;
  }

  tail.next = left ? left : right;

  return head;
};
// @leet end
