# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         stack=[]
#         while head:
#             stack.append(head)
#             head=head.next
            
#         head=stack.pop()
#         node=head
#         while stack:
#             node.next=stack.pop()
#             node=node.next
#         node.next=None
#         return head

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1, p2 = None, head
        while p2 is not None:
            p3,p2.next = p2.next,p1
            p1,p2 = p2,p3

        return p1