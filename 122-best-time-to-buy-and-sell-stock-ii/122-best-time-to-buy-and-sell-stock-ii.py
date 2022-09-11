class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = []
        ans = 0
        for i in prices:
            if not s:
                s.append(i)
                continue
            if s[-1] > i:
                ans += s[-1]-s[0]
                while s:
                    s.pop()
                s.append(i)
            else:
                s.append(i)
                
        if s:
            ans += s[-1] - s[0]
        return ans