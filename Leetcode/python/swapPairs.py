# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
    
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Updating pointers
            prev = first
            head = first.next
        
        return dummy.next
    
    def printList(self, l: Optional[ListNode]) -> None:
        while l:
            print(l.val, end=' ')
            l = l.next
        print()

print("Test case 1")
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
s.printList(s.swapPairs(l)) # 2 1 4 3
print("Test case 2")
l = ListNode(1)
s = Solution()
s.printList(s.swapPairs(l)) # 1