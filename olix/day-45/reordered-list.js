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
  if (!head) return;
  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  let second = slow.next;
  slow.next = null;
  second = reverse(second);
  let first = head;
  while (first && second) {
    let firstNext = first.next;
    let secondNext = second.next;
    first.next = second;
    second.next = firstNext;
    first = firstNext;
    second = secondNext;
  }

  return head;
};

function reverse(head) {
    let prev = null;
    while (head) {
        let next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
    }

console.log(reorderList([1, 2, 3, 4, 5]));