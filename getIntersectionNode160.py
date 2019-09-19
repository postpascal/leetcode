# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        ha=headA
        hb=headB

        n=0
        while n<2:
            if not headA.next:
                headA=hb
                n=n+1
            else:
                headA=headA.next
            
            if not headB.next:
                headB=ha
                n=n+1
            else:
                headB=headB.next
            
        while headB!=headA:
            headB=headB.next
            headA=headA.next
        return headA