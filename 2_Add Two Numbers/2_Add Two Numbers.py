class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.l3=None
    def add(self,val):
        if self.l3==None:
            self.l3=ListNode(val)
        else:
            cur=self.l3
            while cur.next:
                cur=cur.next
            cur.next=ListNode(val)
    def addTwoNumbers(self,l1,l2):
        cur1=l1
        cur2=l2
        next_val=0
        while True:
            now=0
            if cur1==None and cur2==None:
                if next_val>=1:
                    self.add(int(next_val))
                return self.l3
            if cur1:
                now+=cur1.val
                cur1=cur1.next
            else:
                cur1=None
            if cur2:
                now+=cur2.val
                print(cur2.val)
                cur2=cur2.next
            else:
                cur2=None
            now+=next_val
            next_val=now/10
            now=now%10
            self.add(int(now))
