# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(None)
        l = left
        right = ListNode(None)
        r = right

        cur = head
        while cur:
            if cur.val < x:
                newnode = ListNode(cur.val)
                left.next = newnode
                left = left.next
            else:
                newnode = ListNode(cur.val)
                right.next = newnode
                right = right.next
            cur =  cur.next

        left.next = r.next
        # print(l, r)
        return l.next
        