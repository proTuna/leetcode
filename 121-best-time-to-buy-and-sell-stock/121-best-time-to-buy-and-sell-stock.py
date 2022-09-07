class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now = int(1e9)
        ans = 0
        for i in prices:
            if i < now:
                now = i
            else:
                ans = max(ans, i - now)
                
        return ans
            