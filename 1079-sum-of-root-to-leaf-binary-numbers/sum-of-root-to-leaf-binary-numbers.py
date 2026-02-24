# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            path <<= 1
            if node.val:
                path |= 1
            if not node.left and not node.right:
                ans += path
                continue
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
        return ans

