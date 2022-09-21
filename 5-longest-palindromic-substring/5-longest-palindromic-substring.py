class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            # 팰린드롬 판별 및 투 포인터 확장
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        # 해당 사항이 없을 때 빠르게 리턴
        if len(s)<2 or s == s[::-1]:
            return s
        ans = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)-1):
            ans = max(ans, expand(i,i+1),expand(i,i+2),key=len)
        return ans
        
#         lp = ''
#         dp = [[0]*len(s) for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = True
#             lp = s[i]
            
#         for i in range(len(s)-1,-1,-1):
#             for j in range(i+1,len(s)):
#                 if s[i] == s[j]:
#                     if j-i == 1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
                        
#                         if len(lp) < len(s[i:j+1]):
#                             lp = s[i:j+1]
#         return lp