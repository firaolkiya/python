# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        dummy = ListNode(0)
        dummy.next=head
        fast=head
        slow=dummy
        while fast and slow:
            if size>=n:
                slow=slow.next
            fast=fast.next
            size+=1
        if dummy==slow:
                head=head.next
        if slow.next:
            slow.next=slow.next.next
        else:
            slow.next=None
        return head