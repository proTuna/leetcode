# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        mid = l//2
        
        if not l:
            return None
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid+1:])
        )