# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        def count(root, target):
            if not root:
                return 
            target -= root.val

            if target == 0:
                self.ans += 1
            count(root.left, target)
            count(root.right, target)
        def dfs(root):
            if not root:
                return 
            count(root, targetSum)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans