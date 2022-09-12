class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        misses = 1
        cnt = position = 0
        while misses <= n:
            if position < len(nums) and misses >= nums[position]:
                misses += nums[position]
                position += 1
            else:
                misses *=2
                cnt+=1
                
        return cnt
        