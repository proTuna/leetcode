class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        ans = False
        for i in nums:
            d[i] = d.get(i,0) +1
        for k,v in d.items():
            if v>1:
                return True