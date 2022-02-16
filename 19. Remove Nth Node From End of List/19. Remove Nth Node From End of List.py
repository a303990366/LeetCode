# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head=ListNode(next=head)
        cur=new_head
        size=0
        
        while cur.next:
            cur=cur.next
            size+=1
        cur=new_head
        for i in range((size-n)):
            cur=cur.next
        if cur.next!=None:
            cur.next=cur.next.next
        return new_head.next
