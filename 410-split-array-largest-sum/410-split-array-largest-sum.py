class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_n = max(nums)
        sum_n = sum(nums)
        while max_n < sum_n:
            mid = (max_n+sum_n)//2
            total, cnt = 0, 1
            for num in nums:
                if total+num <= mid:
                    total += num
                else:
                    total = num
                    cnt+=1
            if cnt>m:
                max_n = mid+1
            else:
                sum_n = mid
        return sum_n