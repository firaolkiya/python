# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        above_head=None
        below_head=None
        above_tail=None
        below_tail=None
        cur=head
        while cur:
            if cur.val>=x:
                if above_head is None:
                    above_head=cur
                else:
                    above_tail.next=cur
                above_tail=cur
            else:
                if below_head is None:
                    below_head=cur
                else:
                    below_tail.next=cur
                below_tail=cur
            cur=cur.next
        if below_tail:
            below_tail.next=above_head
        else:
            return above_head
        if above_tail:
            above_tail.next=None
        return below_head

