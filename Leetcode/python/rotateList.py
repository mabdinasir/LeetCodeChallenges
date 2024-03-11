from typing import Optional

# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

result1 = Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
result2 = Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)

# Print the values of the linked lists
while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next
print("None")

while result2:
    print(result2.val, end=" -> ")
    result2 = result2.next
print("None")