# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode], k: int) -> Optional[ListNode]:
            count = 0
            current = head
            while current and count < k:
                current = current.next
                count += 1
            if count == k:
                prev = None
                current = head
                for _ in range(k):
                    nextNode = current.next
                    current.next = prev
                    prev = current
                    current = nextNode
                head.next = reverse(current, k)
                return prev
            return head
        return reverse(head, k)

    def printList(self, l: Optional[ListNode]) -> None:
        while l:
            print(l.val, end=' ')
            l = l.next
        print()

print("Test case 1")
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
s.printList(s.reverseKGroup(l, 2)) # 2 1 4 3 5
print("Test case 2")
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
s.printList(s.reverseKGroup(l, 3)) # 3 2 1 4 5