# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        l , r = left-1 , right -1 
        while l <= r:
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        head = ListNode(ans[0])
        cur = head
        for val in ans[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head
