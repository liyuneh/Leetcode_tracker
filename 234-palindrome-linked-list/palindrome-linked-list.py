# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)
        prev , cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        slow , fast = head, prev
        # print(prev)
        while fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True