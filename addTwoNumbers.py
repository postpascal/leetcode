# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		return 6564

def lnmaker(l:list) -> ListNode:
	tail = None
	for i in l[::-1]:
		head = ListNode(i)
		head.next = tail
		tail = head
	return tail


def println(ln):
	while ln.next:
		print(ln.val)
		ln=ln.next
	print(ln.val)

# a = Solution()

# t=a.addTwoNumbers(qq,6)

a = lnmaker([2,4,3])
b = lnmaker([5,6,4])


def l2i(a):
	l=[]
	while a.next:
		l.append(a.val)
		a = a.next
	l.append(a.val)
	l = list(map(str,l))
	i = int(''.join(l))
	return i 

c=str(l2i(a)+l2i(b))
ccc = lnmaker([int(i) for i in c[::-1]])

'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l=[]
        while l1.next:
            l.append(l1.val)
            l1 = l1.next
        l.append(l1.val)
        l = list(map(str,l))
        i = int(''.join(l)[::-1])

        
        
        ll=[]
        while l2.next:
            ll.append(l2.val)
            l2 = l2.next
        ll.append(l2.val)
        ll = list(map(str,ll))
        ii = int(''.join(ll)[::-1])
        
        c=str(int(i)+int(ii))
        
        tail = None
        for i in c:
            head = ListNode(i)
            head.next = tail
            tail = head
        return tail
'''



# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         carry = 0
#         c0 = ListNode((l1.val+l2.val)%10)
#         c=c0
#         carry = (l1.val+l2.val)//10
#         while l1.next and l2.next:
#             c.next=ListNode((l1.next.val+l2.next.val+carry)%10)
#             carry=(l1.next.val+l2.next.val+carry)//10
#             c=c.next
#             l1=l1.next
#             l2=l2.next
#         l=ListNode(l1.val)
#         l.next= l1.next or l2.next
#         while l.next:
#             c.next=ListNode((l.next.val+carry)%10)
#             carry=(l.next.val+carry)//10
#             l=l.next
#             c=c.next
#         if carry>0:
#             c.next=ListNode(1)
#         return c0
