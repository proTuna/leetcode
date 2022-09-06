class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        ans = -1
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return ans if ans != -1 else start 