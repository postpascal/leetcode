# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stackl=[]
        stackr=[]
        nodel=noder=root
        if not root:
            return True
        
        while stackl or stackr or nodel.left or noder.right:
            while nodel.left and noder.right:
                nodel=nodel.left
                noder=noder.right
                if nodel.val!=noder.val:
                    return False
                stackl.append(nodel)
                stackr.append(noder)
            if not nodel.left and not noder.right:
                nodel=stackl.pop()
                noder=stackr.pop()
            else:
                return False

            while not nodel.right and not noder.left:
                if not stackl and not stackr:
                    return True
                else:
                    nodel=stackl.pop()
                    noder=stackr.pop()
            
            nodel=nodel.right
            noder=noder.left
            if not nodel or not noder:
                return False
            if nodel.val !=noder.val:
                return False
            stackl.append(nodel)
            stackr.append(noder)
        return True
        
            
            
            
            
        