from collections import defaultdict

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def inorderTraversal(root):
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

def preorderTraversal(root):
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
			res.append(cur.val)
			cur = cur.left
		else:
			node = stack.pop()
			cur = node.right
		
	return res

def levelOrderTraversal(root):
	d=defaultdict(list)
	def recursiver(root,i):
		if root:
			d[i].append(root.val)
			recursiver(root.left,i+1)
			recursiver(root.right,i+1)
	recursiver(root,0)
	return d.values()


def buildtreeslevelOrder(l=1,i=1,n=4):
	if n==l:
		return None
	n=2**l-i
	node=TreeNode(n)
	node.left=buildtreeslevelOrder(l+1,2*i)
	node.right=buildtreeslevelOrder(l+1,2*i-1)
	return node


print(preorderTraversal(buildtreeslevelOrder()))

