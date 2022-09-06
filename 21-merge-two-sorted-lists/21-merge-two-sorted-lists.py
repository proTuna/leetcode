# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = []
        head = ans = ListNode()
        node1 = list1
        node2 = list2
        while list1 or list2:
            if not list2 or (list1 and list1.val <= list2.val):
                # head.next = list1
                head.next = ListNode(list1.val)
                # head = list1
                list1 = list1.next
            else:
                # head.next = list2
                head.next = ListNode(list2.val)
                # head = list2
                list2 = list2.next
            head = head.next
            
        return ans.next