# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        if p1==None:
            return p2
        elif p2==None:
            return p1
        head=None
        tail=None
        while p1!=None and p2!=None:
            if p1.val<p2.val:
                t1=p1
                if head==None:
                    head=p1
                else:
                    tail.next=p1
                tail=p1
                p1=t1.next
            else:
                t1=p2
                if head==None:
                    head=p2 
                else:
                    tail.next=p2
                tail=p2
                p2=t1.next
        if p1!=None:
            tail.next=p1
        elif p2!=None:
            tail.next=p2
        return head


