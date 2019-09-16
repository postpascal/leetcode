# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        while head:
            if not head.next or not head.next.next:
                return False
            if head==head.next.next:
                return True
            t=head.next
            head.next=head.next.next
            head=t
        return False