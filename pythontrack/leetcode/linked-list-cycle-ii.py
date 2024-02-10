class Solution(object):
    def detectCycle(self, head):
        fast=head
        while fast:
            if fast.val!="slow":
                fast.val="slow"
                fast=fast.next
            else:
                return fast
        return fast