# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        prev = dummy 
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        l  = head
        for _ in range(k - 1):
            l = l.next
        r = head
        for _ in range(count - k):
            r = r.next
        l.val , r.val = r.val, l.val

        return head
            
        