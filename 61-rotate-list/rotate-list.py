# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next
        k = k % n
        if k == 0:
            return head
        
        tail = head
        for i in range(n - k - 1):
            tail = tail.next
        new = tail.next
        tail.next = None
        cur.next = head
        return new