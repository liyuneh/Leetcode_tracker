# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        Sum = 0
        def dfs(root, parent, grand):
            nonlocal Sum
            if not root:
                return 
            if grand is not None and (grand % 2) == 0:
                Sum += (root.val)
            dfs(root.left, root.val , parent)
            dfs(root.right, root.val , parent)
        dfs(root, None, None)
        return Sum
            