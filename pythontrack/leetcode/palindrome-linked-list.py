class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution(object):
    def isPalindrome(self, head):
        current=head
        head1=None
        while current:
            node = Node(current.val)
            node.next=head1
            head1=node
            current=current.next
        list1=head1
        list2=head
        while list1 and list2:
            if not list1.val == list2.val:
                return False
            list1=list1.next
            list2=list2.next
        return True


        