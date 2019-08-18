# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
def maketree(l,i):
	if i>=len(l):
		return None
	if l[i]==None:
		return None
	n=TreeNode(l[i])
	n.left=maketree(l,i+1)
	n.right=maketree(l,i+2)
	return n

class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		
		if not root:
			return res
		
		cur = root
		stack = []
		while len(stack) > 0 or cur:
			
			if cur:
				stack.append(cur)
				cur = cur.left
			else:
				node = stack.pop()
				res.append(node.val)
				cur = node.right
			
		return res


def maketree(l,i):
	if i>=len(l):
		return None
	if l[i]==None:
		return None
	n=TreeNode(l[i])
	n.left=maketree(l,i+1)
	n.right=maketree(l,i+2)
	return n

s=maketree([1,None,2,3],0)


a=Solution()
print(a.inorderTraversal(s))