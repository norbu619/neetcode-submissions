# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        after = temp.next
        before = None

        while temp != None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
        