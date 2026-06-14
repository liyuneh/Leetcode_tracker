# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        cur = fast = head
        while fast and fast.next:
            ans.append(cur.val)
            cur = cur.next
            fast = fast.next.next
        
        total = 0
        while cur:
            total = max(total, cur.val + ans.pop())
            cur = cur.next
        
        return total