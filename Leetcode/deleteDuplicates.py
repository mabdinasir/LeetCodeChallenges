# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        current = head
        while current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

print(Solution().deleteDuplicates([1,1,2])) # [1,2]
print(Solution().deleteDuplicates([1,1,2,3,3])) # [1,2,3]