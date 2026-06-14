# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        count = 0
        cur = head
        while cur:
            ans.append(cur.val)
            count += 1
            cur = cur.next
        total = 0
        for i in range(count):
            total = max(total, ans[i] + ans[count-1-i])
        # print(total)
        return total