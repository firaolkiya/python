
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head=None
        odd_head=None
        even_tail=None
        odd_tail=None
        even=head
        odd=head.next
        while odd or even:
            if even:
                if not even_tail:
                    even_head=even
                else:
                    even_tail.next=even
                even_tail=even
                if even.next:
                    even=even.next.next
                else:
                    even=None
            if odd:
                if not odd_tail:
                    odd_head=odd
                else:
                    odd_tail.next=odd
                odd_tail=odd
                if odd and odd.next:
                    odd=odd.next.next
                else:
                    odd=None
        even_tail.next=odd_head
        odd_tail.next=None
        return head
                



        
        