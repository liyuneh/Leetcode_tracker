# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        ans = []
        while cur:
            count += 1
            ans.append(cur.val)
            cur = cur.next
        ans[k-1] , ans[count- k ] = ans[count - k] , ans[k-1]

        head = ListNode(ans[0])
        cur = head

        for val in ans[1:]:
            cur.next = ListNode(val)
            cur = cur.next 
        return head
