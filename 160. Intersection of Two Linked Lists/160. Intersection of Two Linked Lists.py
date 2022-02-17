class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        sizeA, sizeB = 1, 1
        while cur1.next:
            cur1=cur1.next
            sizeA+=1
        while cur2.next:
            cur2=cur2.next
            sizeB+=1
        dis=abs(sizeA-sizeB)
        if sizeA<=sizeB:
            cur1, cur2 = headA, headB
        else:
            cur1, cur2 = headB, headA
        for i in range(dis):
            cur2=cur2.next
        
        while cur1 and cur2:
            if cur1==cur2:
                return cur1
            cur1=cur1.next
            cur2=cur2.next
        return None
