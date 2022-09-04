class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MAX = -int(1e9)
        cnt = 0
        for i in nums:
            if i == 1:
                cnt+=1
            else:
                MAX = max(MAX,cnt)
                cnt = 0
        MAX = max(MAX,cnt)
        return MAX