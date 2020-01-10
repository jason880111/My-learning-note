# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root is None):
            return True

        self.found = 0

        def preOrder(root):

            if(root is None):
                return 0
            
            if(root.left is None and root.right is None):
                return 1

            left = preOrder(root.left)
            right = preOrder(root.right)
  
            if(abs(right - left) > 1):
                self.found = 1

            return 1+max(left,right)
 
        preOrder(root)
        if(self.found):
            return False
        
        return True
