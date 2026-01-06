# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mx, res, level = float('-inf'), 0 , 0
        ans = deque()
        ans.append(root)
        while ans:
            level += 1
            internal_sum = 0
            for _ in range(len(ans)):
                node = ans.popleft()
                internal_sum += node.val

                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
            if mx < internal_sum:
                mx, res = internal_sum, level
        return res