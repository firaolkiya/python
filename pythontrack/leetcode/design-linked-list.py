class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
        

    def get(self, index):
        i=0
        cur=self.head
        while cur:
            if i==index:
                return cur.val
            i+=1
            cur=cur.next
        return -1
        

    def addAtHead(self, val):
        node =Node(val)
        node.next=self.head
        self.head=node
        if self.tail is None:
            self.tail=node
        

    def addAtTail(self, val):
        node=Node(val)
        if self.head is None:
            self.head=node
        else:
            self.tail.next=node
        self.tail=node
        
    def addAtIndex(self, index, val):
        node=Node(val)
        if self.head is None and index==0:
            self.head=node
            self.tail=node
        elif index==0:
            node.next=self.head
            self.head=node

        else:
            cur=self.head
            for i in range(index-1):
                if not cur:
                    return
                cur=cur.next
            if cur:
                node.next=cur.next
                cur.next=node
                if node.next is None:
                    self.tail=node
    def deleteAtIndex(self, index):
        if index==0 and self.head:
            self.head=self.head.next
            if self.head is None:
                self.tail=None
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            if cur and cur.next:
                if cur.next.next is None:
                    self.tail=cur
                cur.next=cur.next.next
                


        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)