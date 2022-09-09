# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertTree(r: Optional[TreeNode])-> Optional[TreeNode]:
            if r != None:
                r.left, r.right = r.right, r.left
                invertTree(r.left)
                invertTree(r.right)
        node = root
        invertTree(node)
        return root