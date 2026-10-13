# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        dummy = ListNode()
        dummy.next = head

        leftPrev, curr = dummy, head

        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        prev = None
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next

            
        