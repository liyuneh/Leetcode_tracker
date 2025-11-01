# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        index = count - n
        if index == 0:
            return head.next
        cur = head
        for _ in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next

        return head