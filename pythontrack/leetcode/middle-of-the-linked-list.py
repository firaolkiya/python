# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast.next:
            slow=slow.next
            print(fast.val)
            fast=fast.next
            if  not fast.next:
                return slow
            fast=fast.next
        return slow

