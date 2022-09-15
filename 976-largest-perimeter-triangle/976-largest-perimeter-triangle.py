class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(2,len(nums)):
            c = nums[i-2]
            b = nums[i-1]
            a = nums[i]
            if c < a+b:
                ans = max(ans,a+b+c)
        return ans