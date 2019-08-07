# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1.val<l2.val:
			p=ListNode(l1.val)
		else:
			p=ListNode(l2.val)

		
		while l1.next and l2.next:
			if l1.next.val<l2.next.val:
				p.next=ListNode(l1.next.val)
				p=p.next
				l1=l1.next
			else:
				p.next=ListNode(l2.next.val)
				p=p.next
				l2=l2.next
				
		c=l1.next or l2.next
		p.next=c
		return p
			