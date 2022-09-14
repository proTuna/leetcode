# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        # In the leaf, if the set is empty, then its an even palindrome.
        # In the leaf, if the set has 1 element , its an odd palindrome.
        # In th leaf, if the set has > 1 elements, its not a palindrome.
        
        def dfs(node, s):
            if not node:
                return 0
            
            if node.val in s:
                s.remove(node.val)
            else:
                s.add(node.val)
                
            if not node.left and not node.right:
                return 1 if len(s) <=1 else 0
            
            left = dfs(node.left, set(s))
            right = dfs(node.right, set(s))
            
            return left+right
        
        return dfs(root,set())