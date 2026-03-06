# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        cur = dummy.next
        l = dummy.next
        r = dummy
        flag = False
        while cur:
            if r.val < x:
                prev = r
            if not flag and cur.val >= x:
                l = cur
                flag = True
            if cur.val < x and l.val >= x:
                nxt = cur.next
                r.next = cur.next
                cur.next = l
                print(prev.val)
                prev.next = cur
                prev = prev.next
                cur = nxt
            else:
                cur = cur.next
                r = r.next

        return dummy.next