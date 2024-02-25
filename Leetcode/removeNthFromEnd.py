# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(1, n + 2):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    
    def printList(self, head: Optional[ListNode]) -> None:
        while head is not None:
            print(head.val)
            head = head.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
sol = Solution()
sol.printList(sol.removeNthFromEnd(head, n))
