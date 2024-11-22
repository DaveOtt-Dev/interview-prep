# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.val is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        if root.left.val == root.right.val:
            return self.isSymmetricHelper(root.left, root.right)
        
        return False

    def isSymmetricHelper(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1.left is not None and node2.right is not None:
            if node1.left.val != node2.right.val:
                return False
        elif not (node1.left is None and node2.right is None):
            return False

        if node1.right is not None and node2.left is not None:
            if node1.right.val != node2.left.val:
                return False
        elif not (node1.right is None and node2.left is None):
            return False

        return self.isSymmetricHelper(node1.left, node2.right) and self.isSymmetricHelper(node1.right, node2.left)