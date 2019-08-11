class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def lnmaker(l:list) -> ListNode:
	tail = None
	for i in l[::-1]:
		head = ListNode(i)
		head.next = tail
		tail = head
	return tail

class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		i=1
		p0=head

		l=0
		while head:
			l=l+1
			head=head.next
		head=p0

		zn=l-n+1
		if zn==1:
			return head.next

		while head:
			i=i+1
			ph=head
			head=head.next
			if i==zn:
				ph.next=head.next
				break

		return p0


d=lnmaker([1,2,3,4,5])

a=Solution()
w=a.removeNthFromEnd(d,1)

while w:
	print(w.val)
	w=w.next