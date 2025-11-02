# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = []

        while cur:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()

        if not ans:
            return None
        head = ListNode(ans[0])
        cur = head
        for num in ans[1:]:
            cur.next = ListNode(num)
            cur = cur.next
        return head