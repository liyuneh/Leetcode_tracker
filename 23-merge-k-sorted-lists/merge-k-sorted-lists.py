# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for head in lists:
            cur = head
            while cur:
                ans.append(cur.val)
                cur = cur.next
        ans.sort()
        dummy = ListNode(0)
        cur = dummy
        for val in ans:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next