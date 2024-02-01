# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head.next
        tail=head
        while cur:
            temp=head
            prev=head
            if cur.val>=tail.val:
                tail=tail.next
                cur=cur.next
                continue
            while temp.val<cur.val and temp!=cur:
                prev=temp
                temp=temp.next
            tail.next=cur.next
            cur.next=temp
            if temp!=head:
                prev.next=cur
            else:
                head=cur
            cur=tail.next
        return head
            

            
        