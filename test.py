class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


a=[]

b=ListNode(3)
tt=b
a.append(tt)
b.next=66
print(tt.next)
