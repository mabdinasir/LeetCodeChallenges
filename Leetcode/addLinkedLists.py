# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next
    
# Create two linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add the two linked lists
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=",")
    result = result.next
# 7 0 8
