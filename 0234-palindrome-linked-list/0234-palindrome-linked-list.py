# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        if not head or not head.next:
            return True

        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        first, second = head, prev  

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True


        