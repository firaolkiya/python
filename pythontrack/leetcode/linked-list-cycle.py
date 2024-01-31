# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head 
        flag = True
        while fast and fast.next:
            if not flag and slow == fast:
                print(slow.val)
                return True
            flag = False
            slow = slow.next
            fast = fast.next.next
        return False

