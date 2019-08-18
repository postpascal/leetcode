class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
def maketree(l,i=0):
	if i>=len(l):
		return None
	if l[i]==None:
		return None
	n=TreeNode(l[i])
	n.left=maketree(l,i+1)
	n.right=maketree(l,i+2)
	return n

# class Solution:
# 	def isValidBST(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: bool
# 		"""
# 		def helper(node, lower = float('-inf'), upper = float('inf')):
# 			if not node:
# 				return True
			
# 			val = node.val
# 			if val <= lower or val >= upper:
# 				return False

# 			if not helper(node.right, val, upper):
# 				return False
# 			if not helper(node.left, lower, val):
# 				return False
# 			return True

# 		return helper(root)
		
class Solution:
	def isValidBST(self, root):
		def traversalBST(root):
			left_left=root.val
			right_right=root.val
			if root.left:
				if root.val<=root.left.val:
					return [False,False]
				left_left,left_right=traversalBST(root.left)
				if root.val<=left_right:
					return [False,False]
			if root.right:
				if root.val>=root.right.val:
					return [False,False]
				right_left,right_right=traversalBST(root.right)
				if root.val>=right_left:
					return [False,False]
#			print([left_left,right_right])
			return [left_left,right_right]

		if not root:
				return True
			
		a=traversalBST(root)
		if a[0] is False or a[1] is False:
				return False
		else:
				return True


s=maketree([5,1,4,null,null,3,6])


a=Solution()
print(a.inorderTraversal(s))