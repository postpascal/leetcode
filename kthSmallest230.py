def kthSmallest(self, root: TreeNode, k: int) -> int:
        # inorder traverse, stop at k:
        stack = []      
        stack.append(root)
        
		counter = 0
		output = 0
		node = root
        while counter < k:
            # reach all the way down to the left bottom leaf:
            while node.left:
                node = node.left
                stack.append(node)
            # pop out the last node from the stack
            node = stack.pop()
            counter += 1
            output = node.val
			
            # check if the node has any right child; if not, keep popping
            while node.right == None:
                if counter == k:
                    return output
                node = stack.pop()
                counter += 1
                output = node.val
            # now the node has a right child. go to its right child and dig deep to the left tree...
            node = node.right
            stack.append(node)
        return output