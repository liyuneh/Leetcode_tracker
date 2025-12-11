# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, False)]
        res = []
        while stack :
            cur, v = stack.pop()
            if cur:
                if v :
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return len(res)