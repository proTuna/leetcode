class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        ans = []
        if l == 0:
            return ans
        left = 0
        for i in range(1,l+1):
            if i == l or nums[i] != nums[i-1]+1:
                if i-1 == left:
                    ans.append(str(nums[left]))
                else:
                    ans.append("%d->%d"%(nums[left],nums[i-1]))
                left=i
                
        return ans