class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


def buildnodes(l):
	head=ListNode(l[0])
	node=head
	for i in range(1,len(l)):
		node.next=ListNode(l[i])
		node=node.next
	return head


#### Delete Node

def delnode(head,node):
	if node.next:
		node.val=node.next.val
		node.next=node.next.next
	else:
		while head.next.next:
			head=head.next
		head.next=None

def reverKnode(k,head):
	p1=head
	p2=head
	while k:
		p1=p1.next
		k=k-1
	while p1.next:
		p1=p1.next
		p2.p2.next
	return p2


def circlenode(head):
	p1=head.next.next
	p2=head.next
	while p1!=p2:
		p1=p1.next.next
		p2=p2.next
	p2=head
	while p1!=p2:
		p1=p1.next
		p2=p2.next
	return p1


def reversnodes(head):
	p1=None
	c=head
	while head.next:
		p2=c.next
		c.next=p1
		p1=c
		c=p2
	c.next=p1
	return c

def mergenodes(h1,h2):
	if h1.val<h2.val:
		h=h1
		h1=h1.next
	else:
		h=h2
		h2=h2.next
	l=h

	while h1 and h2:
		if h1.val<h2.val:
			l.next=h1
			l=l.next
			h1=h1.next
		else:
			l.next=h2
			l=l.next
			h2=h2.next
	l.next=h1 or h2
	return h


h=mergenodes(buildnodes([1,3,5,6,8]),buildnodes([0,1,2,5,9]))

while h:
	print(h.val)
	h=h.next














