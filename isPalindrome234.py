# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l=0
        node=head
        while head:
            l=l+1
            head=head.next
        if l<2:
            return True
        if l%2==0:
            ll=l/2
            rr=ll+1
        else:
            ll=int(l/2)
            rr=ll+2
        c=0
        p1=None
        while c<ll:
            c=c+1
            p3=node.next
            node.next=p1
            
            p1=node
            node=p3
        node=p1
        tail=p3
        for i in range(int(rr-ll)-1):
            tail=tail.next

        while node and tail:
            if node.val!=tail.val:
                return False
            node=node.next
            tail=tail.next

        if node==None and tail==None:
            return True
        else:
            return False