# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = ans = dummy
        l = 0
        dummy = dummy.next
        while dummy:
            dummy = dummy.next
            l +=1
        c = l-n
        while c:
            if not node.next:
                return None
            node = node.next
            c-=1
        node.next = node.next.next
        
        return ans.next