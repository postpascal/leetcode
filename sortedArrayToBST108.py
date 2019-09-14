# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l,h):
            if h-l==0:
                return TreeNode(nums[l])
            if h-l==1:
                node=TreeNode(nums[h])
                node.left=TreeNode(nums[l])
                return node
            
            mid=int((h+l)/2)
            
            node=TreeNode(nums[mid])
            node.left=helper(l,mid-1)
            node.right=helper(mid+1,h)
            return node
        if not nums:
            return None
        return helper(0,len(nums)-1)