class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		ll=[]
		if l1.val < l2.val:
			p = ListNode(l1.val)
			ll.append(l1.val)
		else:
			p = ListNode(l2.val)
			ll.append(l2.val)

		while l1.next and l2.next:
			if l1.next.val < l2.next.val:
				p.next = ListNode(l1.next.val)
				ll.append(l1.val)
				p = p.next
				l1 = l1.next
			else:
				p.next = ListNode(l2.next.val)
				ll.append(l2.val)
				p = p.next
				l2 = l2.next

		c = l1.next or l2.next
		p.next = c
		return ll


if __name__== '__main__':
	a=[1,2,4]
	b=[1,3,4]
	l1=ListNode(a[0])
	l2=ListNode(b[0])

	for i in a[1:]:
		l1.next=ListNode(i)
		l1=l1.next
	for i in b[1:]:
		l2.next=ListNode(i)
		l2=l2.next
	t= Solution()
	b=t.mergeTwoLists(l1,l2)
