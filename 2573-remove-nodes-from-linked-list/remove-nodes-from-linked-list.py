# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def back(node):
            # print(node)
            if   not node.next: return node
            node.next = back(node.next)
            # print(node.next)
            if node.next and node.val < node.next.val:
                return node.next
            else:
                return node
        return back(head)
            
            