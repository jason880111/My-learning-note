class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def minValueNode(node):
        current = node

        while current.left is not None:
            current = current.left

        return current
    
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root is None:
            return root
        else:
            while root is not None:
                if val <= root.val:
                    if root.left is None:
                        root.left = TreeNode(val)
                        return root.left
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(val)
                        return root.right
                    else:
                        root = root.right
                        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        while self.search(root,target) != None:

            if target < root.val:
                root.left = self.delete(root.left, target)

            elif target > root.val:
                root.right = self.delete(root.right, target)

            else:
                
                if root.right != None:
                    temp = root.right
                    root = None
                    return temp

                elif root.left != None:
                    temp = root.left
                    root = None
                    return temp

                x = self.minRightNode(root.right)

                root.val = x.val

                root.right = self.delete(root.right, x.val)
            
        return root
        
        
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root is None:
               return None
        else:
            if root.val == target:
                return root
            elif root.val < target:
                return self.search(root.right, target)
            else:
                return self.search(root.left, target)
                
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if target == new_val:
                return root
        else: 
                Solution().delete(root,target)
                Solution().insert(root,new_val)
                
        return root
