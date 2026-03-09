# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
    

        dummy = ListNode(None)
        cur = prev
        last = dummy
        mx = 0
        while cur :
            if cur.val >= mx:
                newnode = ListNode(cur.val)
                last.next = newnode
                last = last.next
                mx = cur.val
            cur = cur.next
        pref, cur = None, dummy.next
        while cur:
            nxt = cur.next
            cur.next = pref
            pref = cur
            cur = nxt
        return pref
        # dom = ListNode(0, pref)
        # cur = dom
        # while cur.next and cur.next.val:
        #     cur = cur.next
        # cur.next = None
        # return dom.next