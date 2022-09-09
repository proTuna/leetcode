# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head
        cur = node
        while cur.next!=None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return node.next