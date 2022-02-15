class ListNode:
    
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
    def get(self, index: int) -> int:
        cur=self.head
        for i in range(index):
            if cur.next!=None:
                cur=cur.next
            else:
                return -1
        if self.head !=None:
            return cur.val
        else:return -1

    def addAtHead(self, val: int) -> None:
        self.head=ListNode(val,next=self.head)
        self.size+=1
    def addAtTail(self, val: int) -> None:
        if self.size>0:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=ListNode(val)
            self.size+=1
        else:
            self.addAtHead(val)
        #return self.head
    def addAtIndex(self, index: int, val: int) -> None:
        #print(index,self.size)
        if index==0:
            self.head=ListNode(val,next=self.head)
        else:
            if index<self.size:
                self.size+=1
                cur=self.head
                for i in range(index-1):
                    cur=cur.next
                tmp=cur.next
                cur.next=ListNode(val=val,next=tmp)
            elif index==self.size:
                self.addAtTail(val)
                

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=self.head.next
        elif index<self.size:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            if cur.next!=None:
                if cur.next.next!=None:
                    cur.next=cur.next.next
                else:cur.next=None
