class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def iter_(node):
            if node:
                yield node.val
                yield from iter_(node.left)
                yield from iter_(node.right)
        return not root or all(val == root.val for val in iter_(root))
