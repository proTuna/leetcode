import heapq as hq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 음수인 경우 k 사용
        # 양수인 경우 k 2번 사용
        # 음수가 없고 0이 있다면 k 다사용
        hq.heapify(nums)
        while k:
            num = hq.heappop(nums)
            num -= 2*num
            k-=1
            hq.heappush(nums,num)
            
        return sum(nums)