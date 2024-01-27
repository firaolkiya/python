class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_po = None
        cur_po = head
        while cur_po:
            next_node = cur_po.next
            cur_po.next = pre_po
            pre_po = cur_po
            cur_po = next_node
        return pre_po