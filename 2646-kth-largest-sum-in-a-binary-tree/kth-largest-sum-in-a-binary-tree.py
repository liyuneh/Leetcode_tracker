# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = deque()
        ans.append(root)
        level = 0
        res = []

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
            res.append(internal_sum)
        res.sort(reverse=True)
        if k > len(res):
            return -1
        else:
            return res[k-1]