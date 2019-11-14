# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        s1=head
        s2=head
        while True:
            if s1.next and s2.next and s2.next.next:
                s1=s1.next
                s2=s2.next.next
                if s1==s2:
                    break
            else:
                return 
        s0=head
        while s0 != s1:
            s0=s0.next
            s1=s1.next
        return s0