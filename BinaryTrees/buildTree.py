class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def buildTree(self, preorder, inorder):
	if not preorder or not inorder:
		return None
	
	root = TreeNode(preorder[0])
	ind = inorder.index(root.val)

	left_pre = preorder[1:ind+1]
	left_in = inorder[:ind]
	root.left = self.buildTree(left_pre, left_in)
	

	right_pre = preorder[ind+1:]
	right_in = inorder[ind+1:]
	root.right = self.buildTree(right_pre, right_in)
	
	return root

def buildtreeslevelOrder(l=1,i=1,n=4):
	if n==l:
		return None
	n=2**l-i
	node=TreeNode(n)
	node.left=buildtreeslevelOrder(l+1,2*i)
	node.right=buildtreeslevelOrder(l+1,2*i-1)
	return node
	

def buildTreeIter(self, preorder, inorder):
	def woker(pre,ino):
		if len(pre)<1:
			return None
		if len(pre)==1:
			return TreeNode(pre[0])
		i=0
		while pre[0]!=ino[i] and i<len(ino):
			i+=1

		root=TreeNode(pre[0])
		root.left=woker(pre[1:i+1],ino[:i])
		root.right=woker(pre[i+1:],ino[i+1:])
		return root
	w=woker(preorder,inorder)
	return w