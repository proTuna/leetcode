# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        node = ListNode(-1)
        tmp = node
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        l.reverse()
        for i in l:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return node.next