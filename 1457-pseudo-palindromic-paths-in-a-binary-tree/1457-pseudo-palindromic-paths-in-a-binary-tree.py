# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        # 2번째 풀이
        target = {0,1,2,4,8,16,32,64,128,256} # 1-9까지 이므로
        def dfs(node,s):
            s ^=1 << (node.val-1)
            if not node.left and not node.right: # pseudo-palindromic 하려면 odd 숫자는 1개이하여야한다.
                return int(s in target)
            return (dfs(node.left,s) if node.left else 0) + (dfs(node.right,s) if node.right else 0)
        return dfs(root, 0)
        
        # In the leaf, if the set is empty, then its an even palindrome.
        # In the leaf, if the set has 1 element , its an odd palindrome.
        # In th leaf, if the set has > 1 elements, its not a palindrome.
# 1번째 풀이      
#         def dfs(node, s):
#             if not node:
#                 return 0
            
#             if node.val in s:
#                 s.remove(node.val)
#             else:
#                 s.add(node.val)
                
#             if not node.left and not node.right:
#                 return 1 if len(s) <=1 else 0
            
#             left = dfs(node.left, set(s))
#             right = dfs(node.right, set(s))
            
#             return left+right
        
#         return dfs(root,set())
            