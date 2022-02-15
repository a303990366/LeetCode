class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode(next=head)
        cur=new_head
        while cur.next and cur.next.next:
            first=cur.next #store first node which need to swtich
            second=cur.next.next# store secondd node which need to switch
            tmp=second.next#store second node's next list
            
            cur.next=second# cur->second
            second.next=first #cur->second->first
            cur=first         #...->......-> cur
            cur.next=tmp      #...->......-> cur -> tmp
        return new_head.next
