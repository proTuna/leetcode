# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        ans = self.isSameTree(left, right)
        return ans
        
        
    def isSameTree(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l and r:
            return l.val == r.val and self.isSameTree(l.left, r.right) and self.isSameTree(l.right,r.left)
        else:
            return l == r