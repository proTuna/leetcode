class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            cnt = 0
            while num:
                num //=10
                cnt+=1
            if cnt%2==0:
                ans+=1
        return ans