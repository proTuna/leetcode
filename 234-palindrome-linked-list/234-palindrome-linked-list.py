# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        a = []
        node = head
        while node:
            a.append(node.val)
            node = node.next
        
        l = len(a)
        n = l//2
        ans = True
        
        for i in range(n):
            if a[i] != a[l-i-1]:
                print(i)
                ans = False
                break
            
        
        return ans