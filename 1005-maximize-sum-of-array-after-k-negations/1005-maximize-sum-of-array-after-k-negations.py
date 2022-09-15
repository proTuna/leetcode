import heapq as hq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        while k:
            num = hq.heappop(nums)
            num -= 2*num
            k-=1
            hq.heappush(nums,num)
            
        return sum(nums)