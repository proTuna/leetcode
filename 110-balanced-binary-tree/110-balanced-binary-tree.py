# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 재귀로 높이 차이를 계산해서 푼다.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            
            # 높이 차이가 나는 경우 -1, 이외에는 1씩 증가시켜서 리턴한다.
            if left == -1 or right == -1 or abs(left - right) > 1 :
                return -1
            return 1 + max(left,right)
        
        return check(root) != -1