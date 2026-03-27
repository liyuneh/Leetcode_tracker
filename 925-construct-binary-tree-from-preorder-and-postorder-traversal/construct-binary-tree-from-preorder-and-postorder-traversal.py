# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        track = TreeNode(preorder[0])
        if len(preorder) == 1:
            return track
        left = preorder[1]
        left_index = postorder.index(left) + 1

        track.left = self.constructFromPrePost(preorder[1:left_index + 1], postorder[:left_index])
        track.right = self.constructFromPrePost(preorder[left_index + 1:], postorder[left_index:-1])

        return track
