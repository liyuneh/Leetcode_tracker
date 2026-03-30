# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mx = nums[len(nums) // 2]
        ind = nums.index(mx)
        root = TreeNode(mx)
        root.left = self.sortedArrayToBST(nums[:ind])
        root.right = self.sortedArrayToBST(nums[ind + 1:])
        return root