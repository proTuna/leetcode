# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        
        node = head
        while node:
            a+=1
            node = node.next
            
        mid = a//2 + 1
        
        check = 1
        node2 = head
        while node2:
            if check == mid:
                break
            node2= node2.next
            check +=1
            
        return node2