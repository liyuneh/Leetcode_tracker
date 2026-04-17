# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root, path):
            nonlocal ans
            if not root:
                return 
            path.append(chr(root.val + ord("a")))
            if not root.left and not root.right:
                new = "".join(path)
                new = new[::-1]
                if ans:
                    if ans[-1] > new:
                        ans.pop()
                        ans.append(new)
                else:
                    ans.append(new)
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return ans[0]    