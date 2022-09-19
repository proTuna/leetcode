class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        if len(nums) <3:
            return ans
        else:
            nums.sort()
            
            for i,v in enumerate(nums):
                if i>0 and v == nums[i-1]:
                    continue
                
                l,r = i+1, len(nums)-1
                
                while l<r:
                    ts = v + nums[l] + nums[r]
                    
                    if ts >0:
                        r-=1
                    elif ts < 0:
                        l+=1
                    else:
                        ans.append([v,nums[l],nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
        return ans