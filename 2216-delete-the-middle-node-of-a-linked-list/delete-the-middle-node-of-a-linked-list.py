# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        
        mid_index = count // 2
        cur = head
        for _ in range(mid_index - 1):
            cur = cur.next
        cur.next = cur.next.next

        return head
