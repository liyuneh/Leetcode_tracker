# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        total_nodes = count_nodes(root)
        
        def check(node, index):
            if not node:
                return True
            if index >= total_nodes:
                return False
            return check(node.left, 2*index + 1) and check(node.right, 2*index + 2)
        
        return check(root, 0)
