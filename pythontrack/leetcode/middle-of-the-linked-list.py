# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        size=0
        while curr!=None:
            curr=curr.next
            size+=1
        curr = head
        for i in range(size//2):
            curr=curr.next
        return curr

