# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, path):
            if not node:
                return 
            nonlocal ans
            path <<= 1
            if node.val:
                path |= 1
            if not node.left and not node.right:
                ans += path
                return
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, 0)
        return ans

