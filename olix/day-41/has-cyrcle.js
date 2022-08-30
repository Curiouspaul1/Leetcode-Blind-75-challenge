var hasCycle = function (head) {
  if (!head) return false;
  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
};

console.log(hasCycle([1, 2, 3, 4, 5]));
