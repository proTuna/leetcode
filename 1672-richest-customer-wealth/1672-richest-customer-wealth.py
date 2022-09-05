class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = -int(1e9)
        
        for account in accounts:
            ans = max(sum(account),ans)
            
        return ans