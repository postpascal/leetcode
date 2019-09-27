from collections import defaultdict

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildtreeslevelOrder(l=1,i=1,n=4):
	if n==l:
		return None
	n=2**l-i
	node=TreeNode(n)
	node.left=buildtreeslevelOrder(l+1,2*i)
	node.right=buildtreeslevelOrder(l+1,2*i-1)
	return node

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

# 后序打印二叉树（非递归）
# 使用两个栈结构
# 第一个栈进栈顺序：左节点->右节点->跟节点
# 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
# 第二个栈存储为第一个栈的每个弹出依次进栈
# 最后第二个栈依次出栈

def postOrderTraversal(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)


def levelOrderTraversal(root):
	d=defaultdict(list)
	def recursiver(root,i):
		if root:
			d[i].append(root.val)
			recursiver(root.left,i+1)
			recursiver(root.right,i+1)
	recursiver(root,0)
	return d.values()

class BinaryTree(object):
	def __init__(self, root=None):
		self.root = root

	def is_empty(self):
		return self.root == None

	def preOrder(self,node):
		if node == None:
			return
		# 先打印根结点，再打印左结点，后打印右结点
		print(node.data)
		self.preOrder(node.left)
		self.preOrder(node.right)

	def inOrder(self,node):
		if node == None:
			return
		# 先打印左结点，再打印根结点，后打印右结点
		self.inOrder(node.left)
		print(node.data)
		self.inOrder(node.right)

	def postOrder(self,node):
		if node == None:
			return
		# 先打印左结点，再打印右结点，后打印根结点
		self.postOrder(node.left)
		self.postOrder(node.right)
		print(node.data)
